# https://atcoder.jp/contests/arc105/submissions/25129691

# %%
from functools import reduce

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

N = int(input())
a = list(map(int, input().split()))

print(reduce(gcd, a))
# %%
