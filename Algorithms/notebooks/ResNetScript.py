    def forward(self, x):
        identity = x
        #print(x.shape)      
        x = self.conv1(x)
        #print(x.shape)
        x = self.bn1(x)
        x = F.relu(x)
        x = self.conv2(x)
        #print(x.shape)
        x = self.bn2(x)
        x = F.relu(x)
        x = x + identity
        return x

class KanResWide_X2(nn.Module):
    def __init__(self, input_shape, output_size):
        super(KanResWide_X2, self).__init__()

        #print(input_shape[0])
        #print(input_shape[1])
