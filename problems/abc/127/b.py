# https://atcoder.jp/contests/abc127/submissions/25115879

# %%
r, D, x = map(int, input().split())

for _ in range(10):
    print(x := r*x - D)
# %%
