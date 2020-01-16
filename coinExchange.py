# how many ways can you use buckets of this deomination? 6x + 9y + 20z = N
# The number of things that can be precisely divided into these boxes

def divide6920(m):
    """
    :return:
    """
    ct = []
    n = 1

    while True:
        if 6 + 9 + 20 == m:
            ct.append(n)
        n += 1
        

    return ct


print(divide6920(10))

print(divide6920(100))
print(divide6920(133))
print(divide6920(2))


