# https://atcoder.jp/contests/abc205/submissions/26039921

# %%
N = int(input())
A = sorted(map(int, input().split()))

print("Yes" if A == list(range(1, N+1)) else "No")
# %%
