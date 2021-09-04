# https://atcoder.jp/contests/abc088/submissions/25531176

# %%
N = int(input())
a = sorted(map(int, input().split()), reverse=True)

print(sum(a[::2]) - sum(a[1::2]))
# %%
