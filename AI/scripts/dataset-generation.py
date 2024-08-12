            else:
                raise Exception("Wrong mode in script beginning")

            if np.all([left > 0, right < len(signal)]):
                one_dim_data_dir = osp.join(output_dir, "1D", name, sig_name, label)
                two_dim_data_dir = osp.join(output_dir, "2D", name, sig_name, label)
