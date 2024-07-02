WINDOWS_SIZE = 220
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

qtdb_pkl = 'resources/qtdb_pkl/'
save_path = 'resources/ckpt'

PATH_TO_TEST_MODEL = 'resources/z-score-data/ckpt' + '/epoch_99.ckpt'

if __name__ == '__main__':
    print(DEVICE)
    if DEVICE == 'cuda':
        print(torch.cuda.get_device_name(0))
