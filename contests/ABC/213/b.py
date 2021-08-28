# https://atcoder.jp/contests/abc213/submissions/25308054

# %%
N = int(input())
A = list(map(int, input().split()))

print(A.index(sorted(A)[-2]) + 1)
# %%
