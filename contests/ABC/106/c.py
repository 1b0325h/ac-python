# https://atcoder.jp/contests/abc106/submissions/25345078

# %%
from re import fullmatch

S = fullmatch(r"(1*)(\d*)", input()).groups()
K = int(input())

print(1 if len(S[0]) >= K else S[1][0])
# %%
