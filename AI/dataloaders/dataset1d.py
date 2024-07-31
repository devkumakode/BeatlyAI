        self.mapper = json.load(open(mapping_path))

    def __getitem__(self, index):
        img = np.load(self.data[index]["path"]).astype("float32")
        img = img.reshape(1, img.shape[0])

        return {"image": img, "class": self.mapper[self.data[index]["label"]]}

    def get_dataloader(self, num_workers=4, batch_size=16, shuffle=True):
        data_loader = DataLoader(
