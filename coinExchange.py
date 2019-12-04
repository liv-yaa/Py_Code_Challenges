# how many ways can you use buckets of this deomination? 6x + 9y + 20z = N
# The number of things that can be precisely divided into these boxes

def divide6920():
    """
    :return:
    """
    ct = []
    n = 1

    while True:
        if 6 + 9 + 20 == n:
            ct.append(n)

    return ct



