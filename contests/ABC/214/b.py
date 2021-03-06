# https://atcoder.jp/contests/abc214/submissions/25311915

# %%
from itertools import product

S, T = map(int, input().split())

ans = 0
for a, b, c in product(range(S+1), repeat=3):
    if a+b+c <= S and a*b*c <= T:
        ans += 1

print(ans)
# %%
