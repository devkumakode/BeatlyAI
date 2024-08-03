        identity = x

        out = self.bn1(x)
        out = self.relu(out)
        out = self.conv1(out)

        out = self.bn2(out)
        out = self.relu(out)
        out = self.conv2(out)

        if self.downsample is not None:
            identity = self.downsample(x)
            identity = F.max_pool1d(identity, self.stride)
        else:
            identity = F.max_pool1d(identity, 1)

        out += identity

