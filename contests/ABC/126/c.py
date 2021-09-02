# https://atcoder.jp/contests/abc126/submissions/25511541

# %%
N, K = map(int, input().split())

ans = 0
for i in range(1, N+1):
    cnt = 0
    while i < K:
        cnt += 1
        i *= 2
    ans += 0.5**cnt / N

print(ans)
# %%
