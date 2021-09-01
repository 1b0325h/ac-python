# https://atcoder.jp/contests/abc043/submissions/25478678

# %%
N = int(input())
a = list(map(int, input().split()))

ans = 0
for i in a:
    ans += (i - round(sum(a)/N))**2

print(ans)
# %%
