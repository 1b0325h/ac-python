# https://atcoder.jp/contests/abc209/submissions/25681535

# %%
N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(1, N, 2):
    A[i] -= 1

print("Yes" if sum(A) <= X else "No")
# %%
