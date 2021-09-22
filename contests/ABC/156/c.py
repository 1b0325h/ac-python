# https://atcoder.jp/contests/abc156/submissions/26037820

# %%
from math import inf

N = int(input())
X = list(map(int, input().split()))

ans = inf
for i in range(1, 101):
    ret = 0
    for j in X:
        ret += (j-i)**2
    ans = min(ans, ret)

print(ans)
# %%
