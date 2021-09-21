# https://atcoder.jp/contests/abc180/submissions/26024009

# %%
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

for i in divisors(N):
    print(i)
# %%
