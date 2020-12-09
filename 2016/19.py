# part a)
# from math import *

# part a) is Josephus problem with k=2

n = 3004953

# m = int(log2(n))
# l = n-2**m
# print(2*l+1)

# part b)

# Insight:
# Suppose elves go from 0 to n-1 (inclusive) instead.
# Then let answer for n-1 elves be k.
# We start from the array of elves [0,1,...,n-1].
# m = floor(n/2) is the index of the first elf to be removed in n elves.
# Removing that elf, we have [0,1,...,m-2,m,...,n-1].
# Shifting 0 to the end, we have [1,...,m-2,m,...,n-1,0].
# Now the last elf is simply the kth element in this array.

sol = 0
for k in range(2,n+1):
    toRemove = k//2
    if sol==k-1:
        sol = 0
    else:
        sol = (sol+1 + (sol>=toRemove-1))%k
print(sol+1)
