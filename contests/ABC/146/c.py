# https://atcoder.jp/contests/abc146/submissions/26023532

# %%
def binary_search(ok, ng, f):
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    return ok

A, B, X = map(int, input().split())

def f(N):
    return A*N + B*len(str(N)) <= X

print(binary_search(0, 10**9+1, f))
# %%
