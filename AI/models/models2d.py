def ResNet34(num_classes=8):
    model = models.resnet34()
    model.fc = nn.Linear(model.fc.in_features, num_classes)
    return model


def ShuffleNet(num_classes=8):
    model = models.shufflenet_v2_x1_0()
    model.fc = nn.Linear(model.fc.in_features, num_classes)
