            nn.Dropout(0.5),
            nn.Linear(2048, num_classes),
        )

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), 16 * 16 * 256)
        x = self.classifier(x)
        return x


class MobileNetV2(models.MobileNetV2):
    def __init__(self, num_classes=8):
        super().__init__(num_classes=num_classes)


class AlexNet(models.AlexNet):
