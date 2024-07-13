malignant_data = np.loadtxt(open('datasets/processed/malignant-ventricular-ectopy.csv', 'r'), skiprows=1)
arrhy_data = arrhy_data[:len(malignant_data)]
arrhy_len = len(arrhy_data)/500

i = 0
X_train = []
inter_X_train = []
inter_y_train = []
