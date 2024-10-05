    def __init__(self):
        base_path = './'
        dataset_path = './Dataset'
        classes = ['NSR', 'APB', 'AFL', 'AFIB', 'SVTA', 'WPW', 'PVC', 'Bigeminy',
                   'Trigeminy', 'VT', 'IVR', 'VFL', 'Fusion', 'LBBBB', 'RBBBB', 'SDHB', 'PR']
        ClassesNum = len(classes)
        X = list()
        y = list()

        for root, dirs, files in os.walk(dataset_path, topdown=False):
            for name in files:
                data_train = scio.loadmat(
                    os.path.join(root, name))  # 取出字典里的value

        # arr -> list
                data_arr = data_train.get('val')
                data_list = data_arr.tolist()
                X.append(data_list[0])  # [[……]] -> [ ]
                y.append(int(os.path.basename(root)[0:2]) - 1)

        X = np.array(X)
        y = np.array(y)
        X = standardization(X)
        X = X.reshape((1000, 1, 3600))
        y = y.reshape((1000))
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.5)
        #print("X_val  : ", len(X_val))
        #print("shape of X_val : ", np.shape(X_val))
        #print("shape of y_val : ", np.shape(y_val))
        self.len = X_val.shape[0]  # 取第0元素：长度
        self.x_val = torch.from_numpy(X_val).float().to("cuda")
        self.y_val = torch.from_numpy(y_val).long().to("cuda")

    def __getitem__(self, index):
        return self.x_val[index], self.y_val[index]  # 返回对应样本即可

    def __len__(self):
        return self.len


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, default='./data',
                        help='ECG dataset directory')
    parser.add_argument('--val_size', type=int, default=200,
                        help='the number of samples in validation dataset')
    parser.add_argument('--model_ori', type=str, default='./ECGNet_model_ori.pth',
                        help='the file of the original full precision ECGNet model')
    parser.add_argument('--model', type=str, default='./ECGNet_model.pth',
                        help='the file of the quantized ECGNet model')
    parser.add_argument('--PRETRAIN', action='store_true',
                        help='train the original full precision ECGNet model')  # 全精度
    parser.add_argument('--ALQ', action='store_true',
                        help='adaptive loss-aware quantize ECGNet model')       # ALQ
    parser.add_argument('--POSTTRAIN', action='store_true',
                        help='posttrain the final quantized ECGNet model')
    parser.add_argument('--lr', type=float, default=3e-4,
                        help='learning rate')
    parser.add_argument('--R', type=int, default=15,
                        help='the number of outer iterations, also the number of pruning')
    parser.add_argument('--epoch_prune', type=int, default=1,
                        help='the number of epochs for pruning')
    parser.add_argument('--epoch_basis', type=int, default=8,
                        help='the number of epochs for optimizing bases')
    parser.add_argument('--ld_basis', type=float, default=0.8,
                        help='learning rate decay factor for optimizing bases')
    parser.add_argument('--epoch_coord', type=int, default=10,
                        help='the number of epochs for optimizing coordinates')
    parser.add_argument('--ld_coord', type=float, default=0.8,
                        help='learning rate decay factor for optimizing coordinates')
    parser.add_argument('--wd', type=float, default=0.,
                        help='weight decay')
    parser.add_argument('--pr', type=float, default=0.7,    # prune ratio
                        help='the pruning ratio of alpha')
    parser.add_argument('--top_k', type=float, default=0.005,
                        help='the ratio of selected alpha in each layer for resorting')
    parser.add_argument('--structure', type=str, nargs='+', choices=['channelwise', 'kernelwise', 'pixelwise', 'subchannelwise'],
                        default=['kernelwise', 'kernelwise', 'kernelwise', 'kernelwise', 'kernelwise',
                                 'kernelwise', 'kernelwise', 'subchannelwise', 'subchannelwise'],
                        help='the structure-wise used in each layer')
    parser.add_argument('--subc', type=int, nargs='+', default=[0, 0, 0, 0, 0, 0, 0, 2, 1],  # Matters!!
                        help='number of subchannels when using subchannelwise')
    parser.add_argument('--max_bit', type=int, nargs='+', default=[7, 7, 6, 6, 6, 6, 6, 6, 6],
                        help='the maximum bitwidth used in initialization')
    parser.add_argument('--batch_size', type=int, default=16,
                        help='the number of training samples in each batch')
    args = parser.parse_args()

    # Prepare Dataset
    batch_size = 16
    train_dataset = MyDataset()
    test_dataset = TestDataset()
    val_dataset = ValDataset()
    train_loader = DataLoader(dataset=train_dataset,
                              batch_size=batch_size,
                              shuffle=True,
                              num_workers=0)
    print("Train_loader ready...")
    test_loader = DataLoader(dataset=test_dataset,
                             batch_size=batch_size,
                             shuffle=True,
                             num_workers=0)
    print("Test_loader ready...")
    val_loader = DataLoader(dataset=val_dataset,
                            batch_size=batch_size,
                            shuffle=True,
                            num_workers=0)
    # 全精度 FULL
    if args.PRETRAIN:
        print('pretraining...')
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        net = ECGNet().to(device)
        from torchsummary import summary
        summary(net, input_size=(1, 3600))

        # Construct Loss and Optimizer
        loss_func = torch.nn.CrossEntropyLoss().cuda()
        #optimizer = torch.optim.SGD(net.parameters(), lr=5e-2, momentum=0.5)
        optimizer = optim.Adam(net.parameters(
        ), lr=3e-4, betas=(0.9, 0.999), eps=1e-08, weight_decay=0.0, amsgrad=False)

        get_accuracy(net, train_loader, loss_func)
        val_accuracy = validate(net, val_loader, loss_func)
        best_acc = val_accuracy[0]
        test(net, test_loader, loss_func)
        save_model_ori(args.model_ori, net, optimizer)

        for epoch in range(100):
            # if epoch%30 == 0:
            #    optimizer.param_groups[0]['lr'] *= 0.9
            train_fullprecision(net, train_loader, loss_func, optimizer, epoch)
            val_accuracy = validate(net, val_loader, loss_func)
            if val_accuracy[0] > best_acc:
                best_acc = val_accuracy[0]
                test(net, test_loader, loss_func)
                save_model_ori(args.model_ori, net, optimizer)

    # ALQ
    if args.ALQ:
        print('adaptive loss-aware quantization...')

        net = ECGNet().cuda()
        loss_func = torch.nn.CrossEntropyLoss().cuda()

        print('loading pretrained full precision ECGNet model ...')
