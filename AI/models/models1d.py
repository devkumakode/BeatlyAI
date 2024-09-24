        self.conv2 = conv_block(planes, planes)
        self.bn2 = norm_layer(planes)
        self.dropout = nn.Dropout()
        self.downsample = downsample
        self.stride = stride

    def forward(self, x):
        identity = x
