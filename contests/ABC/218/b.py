# https://atcoder.jp/contests/abc218/submissions/26037981

# %%
P = list(map(int, input().split()))

ans = ""
for i in P:
    ans += chr(96 + i)

print(ans)
# %%
