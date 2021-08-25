# https://atcoder.jp/contests/abc183/submissions/25167953

# %%
from itertools import permutations

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in permutations(range(1, N)):
    cnt = ret = 0
    for j in i:
        cnt += T[ret][j]
        ret = j
    cnt += T[ret][0]
    if cnt == K:
        ans += 1

print(ans)
# %%
