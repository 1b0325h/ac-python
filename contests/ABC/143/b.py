# https://atcoder.jp/contests/abc143/submissions/25482353

# %%
from itertools import combinations

N = int(input())
d = list(map(int, input().split()))

ans = 0
for i, j in combinations(d, 2):
    ans += i * j

print(ans)
# %%
