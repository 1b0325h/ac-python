# https://atcoder.jp/contests/abc049/submissions/25345348

# %%
from re import fullmatch

S = fullmatch(r"(dream(er)?|eraser?)+", input())

print("YES" if S else "NO")
# %%
