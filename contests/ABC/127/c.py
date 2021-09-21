# https://atcoder.jp/contests/abc127/submissions/26022371

# %%
def imos(l, r, add, p=0):
    if isinstance(add, int):
        add = [add] * len(l)
    r = [i+p for i in r]
    table = [0] * (max(r)+2)
    for i in range(len(l)):
        table[l[i]] += add[i]
        table[r[i]] -= add[i]
    for i in range(1, max(r)+2):
        table[i] += table[i-1]
    return table

N, M = map(int, input().split())
LR = [map(int, input().split()) for _ in range(M)]
L, R = [list(_) for _ in zip(*LR)]

print(imos(L, R, 1, 1).count(M))
# %%
