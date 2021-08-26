# https://atcoder.jp/contests/abc083/submissions/25342274

# %%
X, Y = map(int, input().split())

ans = 0
while X*2**ans <= Y:
    ans += 1

print(ans)
# %%
