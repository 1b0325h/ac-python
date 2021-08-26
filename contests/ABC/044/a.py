# https://atcoder.jp/contests/abc044/submissions/25327246

# %%
N, K, X, Y = [int(input()) for _ in range(4)]

print(min(N, K)*X + max(0, N-K)*Y)
# %%
