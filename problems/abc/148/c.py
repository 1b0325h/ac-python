# https://atcoder.jp/contests/abc148/submissions/25163769

# %%
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

A, B = map(int, input().split())

print(lcm(A, B))
# %%
