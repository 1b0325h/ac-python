# https://atcoder.jp/contests/abc123/submissions/25324607

# %%
from math import ceil

N, *A = [int(input()) for _ in range(6)]

print(ceil(N/min(A)) + 4)
# %%
