# https://atcoder.jp/contests/abc220/submissions/26180712

# %%
A, B, C = map(int, input().split())

for i in range(A, B+1):
    if not i % C:
        print(i)
        break
else:
    print(-1)
# %%
