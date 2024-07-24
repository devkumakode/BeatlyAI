val_size = 0.1  # [0, 1]

output_path = "/".join(data_path.split("/")[:-5])
random_state = 7

if __name__ == "__main__":
    dataset = []
    files = glob(data_path)
