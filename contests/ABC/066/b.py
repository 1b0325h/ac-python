# https://atcoder.jp/contests/abc066/submissions/25345525

# %%
from re import search

S = search(r"(.+)\1", input()[:-1]).group()

print(len(S))
# %%
