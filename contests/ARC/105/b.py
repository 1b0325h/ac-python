# https://atcoder.jp/contests/arc105/submissions/26024666

# %%
from functools import reduce

def igcd(x, y):
    while y:
        x, y = y, x%y
    return x

N = int(input())
a = list(map(int, input().split()))

print(reduce(igcd, a))
# %%
