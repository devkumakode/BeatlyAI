    return model


def EfficientNetB4(num_classes=8):
    model = efficientnet.from_name("efficientnet-b4")
    model._fc = nn.Linear(model._fc.in_features, num_classes)
    return model
