# https://atcoder.jp/contests/abc180/submissions/25165904

# %%
from math import inf
from scipy.spatial.distance import minkowski

N = int(input())
x = list(map(int, input().split()))

print(minkowski(0, x, 1))
print(minkowski(0, x, 2))
print(minkowski(0, x, inf))
# %%
