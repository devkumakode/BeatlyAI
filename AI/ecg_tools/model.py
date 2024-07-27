                    MLP(embed_size, expansion),
                    nn.Dropout(dropout)
                ]))
            ]
        )


class Classifier(nn.Sequential):
    def __init__(self, embed_size, num_classes):
        super().__init__(*[
            Reduce("b n e -> b e", reduction="mean"),
            nn.Linear(embed_size, embed_size),
            nn.LayerNorm(embed_size),
            nn.Linear(embed_size, num_classes)
        ])


class ECGformer(nn.Module):

    def __init__(self, num_layers, signal_length, num_classes, input_channels, embed_size, num_heads, expansion) -> None:
