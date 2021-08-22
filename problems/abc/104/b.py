# https://atcoder.jp/contests/abc104/submissions/25135019

# %%
from re import fullmatch

S = input()

print("AC" if fullmatch(r"A[a-z]+C[a-z]+", S) else "WA")
# %%
