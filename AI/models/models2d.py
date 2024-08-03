        super().__init__(num_classes=num_classes)


def VGG16(num_classes=8):
    model = models.vgg16_bn()
    model.classifier[-1] = nn.Linear(model.classifier[-1].in_features, num_classes)
