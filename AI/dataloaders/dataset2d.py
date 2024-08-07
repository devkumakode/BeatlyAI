        self.mapper = json.load(open(mapping_path))

    def __getitem__(self, index):
        img = cv2.imread(self.data[index]["path"])
        img = augment(**{"image": img})["image"]

        return {"image": img, "class": self.mapper[self.data[index]["label"]]}

    def get_dataloader(self, num_workers=4, batch_size=16, shuffle=True):
        data_loader = DataLoader(
            self, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers,
        )
        return data_loader
