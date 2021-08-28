# https://atcoder.jp/contests/abc210/submissions/25287053

# %%
N, A, X, Y = map(int, input().split())

print(A*X + (N-A)*Y if N > A else N*X)
# %%
