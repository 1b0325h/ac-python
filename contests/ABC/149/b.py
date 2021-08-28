# https://atcoder.jp/contests/abc149/submissions/25130857

# %%
A, B, K = map(int, input().split())

print(max(0, A-K), max(0, min(B, A+B-K)))
# %%
