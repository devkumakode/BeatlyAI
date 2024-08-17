    def process_y(self, y):
        # TODO, awni, fix hack pad with noise for cinc
        y = pad([[self.class_to_int[c] for c in s] for s in y], val=3, dtype=np.int32) 
        y = keras.utils.np_utils.to_categorical(
                y, num_classes=len(self.classes))
        return y

def pad(x, val=0, dtype=np.float32):
    max_len = max(len(i) for i in x)
    padded = np.full((len(x), max_len), val, dtype=dtype)
    for e, i in enumerate(x):
