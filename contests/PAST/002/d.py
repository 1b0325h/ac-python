# https://atcoder.jp/contests/past202004-open/submissions/25648099

# %%
from itertools import product
from re import search
from string import ascii_lowercase

S = input()

ans = 0
for i in range(1, 4):
    for j in product(ascii_lowercase+".", repeat=i):
        if search("".join(j), S):
            ans += 1

print(ans)
# %%
