    """Construct a look-up-table to store bitwise values of all intergers given a bitwidth."""
    bit_table = -torch.ones((2**bit, bit), dtype=torch.int8)
    for i in range(1,2**bit):
        for j in range(bit):
            if (i & (1<<j)):
                bit_table[i,j] = 1
    return bit_table.to('cuda')


def binarize(input_t): 
    """Binarize input tensor."""
    dim = input_t.nelement()
    output_t = torch.ones(dim)
    output_t[input_t<0] = -1
    return output_t
