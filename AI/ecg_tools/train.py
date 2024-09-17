        print(f"VALIDATION Accuracy: {accuracy / len(loader) / self.config.dataset.batch_size}")
        print(self.metrics[Mode.eval].confusion_matrix())
        return self.metrics[Mode.eval].confusion_matrix_image()


if __name__ == "__main__":
    cm = ECGClassifierTrainer(EcgConfig()).train()
    plt.figure(dpi=300)
    plt.subplot(1, 2, 1)
    plt.imshow(cm[Mode.train])
    plt.subplot(1, 2, 2)
