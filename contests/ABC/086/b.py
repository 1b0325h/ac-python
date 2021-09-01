# https://atcoder.jp/contests/abc086/submissions/25461322

# %%
from math import sqrt

a, b = input().split()

print("Yes" if sqrt(int(a+b)).is_integer() else "No")
# %%
