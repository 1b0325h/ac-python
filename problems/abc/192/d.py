# https://atcoder.jp/contests/abc192/submissions/25152551

# %%
def base_10(n, base):
    x, c = list(n), 0
    while x:
        c *= base
        c += int(x.pop(0))
    return c

def binary_search(ng, ok, f):
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    return ok

X = input()
M = int(input())

def f(n):
    return base_10(X, n) <= M

if len(X) == 1 and int(X) <= M:
    print(1)
else:
    print(max(binary_search(M+1, 0, f) - int(max(X)), 0))
# %%
