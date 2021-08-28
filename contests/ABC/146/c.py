# https://atcoder.jp/contests/abc146/submissions/25135695

# %%
def binary_search(ng, ok, f):
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    return ok

A, B, X = map(int, input().split())

print(binary_search(10**9+1, 0, lambda n: A*n + B*len(str(n)) <= X))
# %%
