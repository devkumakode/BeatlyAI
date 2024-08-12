                os.makedirs(one_dim_data_dir, exist_ok=True)
                os.makedirs(two_dim_data_dir, exist_ok=True)

                filename = osp.join(one_dim_data_dir, "{}.npy".format(peak))
                np.save(filename, signal[left:right])
                filename = osp.join(two_dim_data_dir, "{}.png".format(peak))

