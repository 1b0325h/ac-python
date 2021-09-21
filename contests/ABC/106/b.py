# https://atcoder.jp/contests/abc106/submissions/26021854

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

ans = 0
for i in range(1, N+1, 2):
    if len(divisors(i)) == 8:
        ans += 1

print(ans)
# %%
