if __name__ == "__main__":
    print(LinearEmbedding(3, 192)(torch.rand(2, 128, 3)).shape)
    print(MLP(3)(torch.rand(2, 128, 3)).shape)
    print(TransformerEncoderLayer(192, 8)(torch.rand(2, 128, 192)).shape)
    print(ECGformer(
        4, 128, 5, 3, 192, 8, 4
