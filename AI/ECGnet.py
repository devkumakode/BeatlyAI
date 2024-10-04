            X, y, test_size=0.2)
        #print("X_test  : ", len(X_test))
        #print("shape of X_test : ", np.shape(X_test))
        #print("shape of y_test : ", np.shape(y_test))
        self.len = X_test.shape[0]  # 取第0元素：长度
        self.x_test = torch.from_numpy(X_test).float().to("cuda")
        self.y_test = torch.from_numpy(y_test).long().to("cuda")

    def __getitem__(self, index):
        return self.x_test[index], self.y_test[index]  # 返回对应样本即可

    def __len__(self):
        return self.len


class ValDataset(Dataset):
