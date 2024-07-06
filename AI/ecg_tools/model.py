            nn.Linear(input_channels, output_channels),
            nn.LayerNorm(output_channels),
            nn.GELU()
        ])
        self.cls_token = nn.Parameter(torch.randn(1, output_channels))

    def forward(self, x):
