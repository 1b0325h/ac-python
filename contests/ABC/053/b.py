# https://atcoder.jp/contests/abc053/submissions/25345302

# %%
from re import search

s = search(r"A[A-Z]*Z", input()).group()

print(len(s))
# %%
