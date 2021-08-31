# https://atcoder.jp/contests/abc186/submissions/25292392

# %%
N = int(input())

ans = 0
for i in range(N+1):
    if "7" in str(i) + oct(i):
        ans += 1

print(N - ans)
# %%
