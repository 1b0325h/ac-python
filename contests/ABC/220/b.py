# https://atcoder.jp/contests/abc220/submissions/26180869

# %%
def decimal(s, b):
    x, c = list(s), 0
    while x:
        c *= b
        c += int(x.pop(0))
    return c

K = int(input())
A, B = input().split()

print(decimal(A, K) * decimal(B, K))
# %%
