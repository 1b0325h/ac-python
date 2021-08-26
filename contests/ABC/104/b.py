# https://atcoder.jp/contests/abc104/submissions/25345186

# %%
from re import fullmatch

S = fullmatch(r"A[a-z]+C[a-z]+", input())

print("AC" if S else "WA")
# %%
