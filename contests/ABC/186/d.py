# https://atcoder.jp/contests/abc186/submissions/25292774

# %%
N = int(input())
A = sorted(map(int, input().split()))

ans, ret = 0, A[0]
for i in range(1, N):
    ans += A[i]*i - ret
    ret += A[i]

print(ans)
# %%
