
        self.classifier = nn.Linear(8, num_classes)

    def forward(self, x):
        out_up = self.features_up(x)
        out_down = self.features_down(x)
        out_middle = out_up + out_down

        out = self.classifier(out_middle)

        return out
