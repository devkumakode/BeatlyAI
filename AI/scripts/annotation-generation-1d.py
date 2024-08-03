
classes = ["N", "V", "\\", "R", "L", "A", "!", "E"]
lead = "MLII"
extension = "npy"  # or `png` for 2D
data_path = osp.abspath("../data/*/*/*/*/*.{}".format(extension))
val_size = 0.1  # [0, 1]

output_path = "/".join(data_path.split("/")[:-5])
random_state = 7

