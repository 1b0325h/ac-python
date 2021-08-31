# https://atcoder.jp/contests/abc186/submissions/25293182

# %%
def extgcd(a, b):
    if not a:
        return (b, 0, 1)
    d, y, x = extgcd(b%a, a)
    return (d, x-b//a*y, y)

def crt(rem, mod):
    r, m = 0, 1
    for i in range(len(rem)):
        x, y, _ = extgcd(m, mod[i])
        if (a := rem[i]-r) % x:
            return (-1, 0)
        r += m * (a//x*y % (mod[i]//x))
        m *= mod[i]//x
    return (r%m, m)

T = int(input())
NSK = [map(int, input().split()) for _ in range(T)]

for N, S, K in NSK:
    print(crt([0, N-S], [K, N])[0] // K)
# %%
