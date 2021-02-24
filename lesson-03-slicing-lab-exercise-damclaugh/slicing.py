
def exchange_first_last(seq):
    swapped = seq[-1:] + seq[1:-1] + seq[0:1]
    return swapped

def every_other_removed(seq):
    every_other = seq[::2]
    return every_other

def first4_last4_every_other_removed(seq):
    firstlast = seq[4:-4]
    every_other = firstlast[::2]
    return every_other

def seq_reversed(seq):
    seq = seq[::-1]
    return seq

def last_third_first_third_mid_third(seq):
    third = int(len(seq)/3)
    last_third = seq[-third:]
    first_third = seq[0:third]
    mid_third = seq[third:-third]
    new_string = last_third + first_third + mid_third
    return new_string