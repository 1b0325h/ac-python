# https://atcoder.jp/contests/abc192/submissions/25151612

# %%
N, K = input().split()

for _ in range(int(K)):
    N = "".join(sorted(N))
    N = str(int(N[::-1]) - int(N))

print(N)
# %%
