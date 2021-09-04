# https://atcoder.jp/contests/abc165/submissions/25532648

# %%
X = int(input())

y, cnt = 100, 0
while y < X:
    y += y // 100
    cnt += 1

print(cnt)
# %%
