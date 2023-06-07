i = 0
L1 = [ 'p', 'e', 'i', 'i', 'm', 'r', 'a', 'r']
L2 = [ 5, 3, 4, 7, 1, 2, -1, 6]
# -i   -8   -7   -6   -5   -4   -3  -2   -1
# i     0    1    2    3    4    5   6    7

while i >= 0:
    print(L1[i], end="")
    i = L2[i]

# Elementos da lista L
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# Indices da lista L
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9