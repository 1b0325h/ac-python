# https://atcoder.jp/contests/arc110/submissions/25129563

# %%
from functools import reduce

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

N = int(input())

print(reduce(lcm, range(2, N+1)) + 1)
# %%
