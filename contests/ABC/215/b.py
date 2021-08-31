# https://atcoder.jp/contests/abc215/submissions/25323821

# %%
N = int(input())

ans = 0
for i in reversed(range(100)):
    if 2**i <= N:
        ans = i
        break

print(ans)
# %%
