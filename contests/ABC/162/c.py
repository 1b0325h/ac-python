# https://atcoder.jp/contests/abc162/submissions/26023783

# %%
from functools import reduce
from itertools import product

def igcd(x, y):
    while y:
        x, y = y, x%y
    return x

K = int(input())

ans = 0
for i in product(range(1, K+1), repeat=3):
    ans += reduce(igcd, i)

print(ans)
# %%
