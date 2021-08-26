# https://atcoder.jp/contests/abc084/submissions/25345383

# %%
from re import fullmatch

A, B = map(int, input().split())
S = fullmatch(rf"\d{{{A}}}-\d{{{B}}}", input())

print("Yes" if S else "No")
# %%
