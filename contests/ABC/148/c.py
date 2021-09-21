# https://atcoder.jp/contests/abc148/submissions/26023651

# %%
def ilcm(x, y):
    u, v = x, y
    while y:
        x, y = y, x%y
    return u*v // x

A, B = map(int, input().split())

print(ilcm(A, B))
# %%
