# https://atcoder.jp/contests/abc216/submissions/25457909

# %%
X, Y = map(int, input().split("."))

print(f"{X}{'-' if Y <= 2 else '' if Y <= 6 else '+'}")
# %%
