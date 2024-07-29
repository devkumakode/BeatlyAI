        x = self.bn2(x)
        x = F.relu(x)
        return x

class KanResModule(nn.Module):
    def __init__(self, in_channels, filterno_1, filterno_2, filtersize_1, filtersize_2, stride):
        super(KanResModule, self).__init__()
        # have to use same padding to keep the size of the input and output the same
        # calculate the padding needed for same
        padding = (filtersize_1 - 1) // 2 + (stride - 1)
        self.conv1 = nn.Conv1d(in_channels, filterno_1, filtersize_1, stride=stride, padding='same')
        self.bn1 = nn.BatchNorm1d(filterno_1)
        self.conv2 = nn.Conv1d(filterno_1, filterno_2, filtersize_2, padding='same')
        self.bn2 = nn.BatchNorm1d(filterno_2)
        
