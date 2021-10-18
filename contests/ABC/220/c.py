# https://atcoder.jp/contests/abc220/submissions/26182272

# %%
def binary_search(ok, ng, f):
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    return ok

N = int(input())
A = list(map(int, input().split()))
X = int(input())

def f(n):
    q, r = divmod(n, N)
    n = q * sum(A)
    for i in range(r):
        n += A[i]
    return n > X

print(binary_search(10**18+1, 0, f))
# %%
