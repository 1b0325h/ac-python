# https://atcoder.jp/contests/arc110/submissions/26024772

# %%
from functools import reduce

def ilcm(x, y):
    u, v = x, y
    while y:
        x, y = y, x%y
    return u*v // x

N = int(input())

print(reduce(ilcm, range(2, N+1)) + 1)
# %%
