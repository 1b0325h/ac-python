# https://atcoder.jp/contests/abc162/submissions/25117035

# %%
from functools import reduce
from itertools import product

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

K = int(input())

ans = 0
for i in product(range(1, K+1), repeat=3):
    ans += reduce(gcd, i)

print(ans)
# %%
