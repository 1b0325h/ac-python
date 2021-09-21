# https://atcoder.jp/contests/abc192/submissions/26024471

# %%
def decimal(s, b):
    x, c = list(s), 0
    while x:
        c *= b
        c += int(x.pop(0))
    return c

def binary_search(ok, ng, f):
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
    return decimal(X, n) <= M

if len(X) == 1 and int(X) <= M:
    print(1)
else:
    print(max(binary_search(0, M+1, f) - int(max(X)), 0))
# %%
