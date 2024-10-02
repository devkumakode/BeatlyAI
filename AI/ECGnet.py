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
        X_train, X_test, y_train, y_test = train_test_split(
