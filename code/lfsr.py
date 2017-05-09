import numpy as np

def lfsr_bits(taps, seed):
    """generate LFSR bitstream
    eg. PRBS7 = X^7 + X^6 + 1 , taps = [7,6]
    """

    val      = int(seed)
    num_taps = max(taps)
    mask     = (1 << num_taps) - 1
    #print val,num_taps,mask

    while(True):
        xor_res = reduce(lambda x, b: x ^ b, [bool(val & (1 << (tap - 1))) for tap in taps])
        val     = (val << 1) & mask  # Just to keep 'val' from growing without bound.
        if(xor_res):
            val += 1
        yield(val & 1)

def prbs7(pat_len=127,seed=1):
    bit_gen = lfsr_bits([7,6],seed)
    bits = []
    for i in range(pat_len):
        bits.append(bit_gen.next())
    return np.array(bits)


def prbs15(pat_len=32767,seed=1):
    bit_gen = lfsr_bits([15,14],seed)
    bits = []
    for i in range(pat_len):
        bits.append(bit_gen.next())
    return np.array(bits)

