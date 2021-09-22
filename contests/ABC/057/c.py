# https://atcoder.jp/contests/abc057/submissions/26041456

# %%
from math import inf

def divisors(n):
    n = abs(n)
    x, i = set(), 1
    while i**2 <= n:
        if not n % i:
            x.add(i)
            x.add(n//i)
        i += 1
    return sorted(x)

N = int(input())

def f(a, b):
    return max(len(str(a)), len(str(b)))

ans = inf
for i in divisors(N):
    ans = min(ans, f(N//i, i))

print(ans)
# %%
