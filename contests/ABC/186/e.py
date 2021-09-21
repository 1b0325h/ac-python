# https://atcoder.jp/contests/abc186/submissions/26024331

# %%
def crt(m, v):
    r, u = 0, 1
    def _f(x, y):
        if not x:
            return (y, 0, 1)
        u, v, w = _f(y%x, x)
        return (u, w-y//x*v, v)
    for i in range(len(v)):
        x, y, _ = _f(u, m[i])
        if (w := v[i]-r) % x:
            return (-1, 0)
        r += u*(w//x*y%(m[i]//x))
        u *= m[i]//x
    return (r%u, u)

T = int(input())
NSK = [map(int, input().split()) for _ in range(T)]

for N, S, K in NSK:
    print(crt([K, N], [0, N-S])[0] // K)
# %%
