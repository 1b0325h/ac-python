# https://atcoder.jp/contests/abc183/submissions/26024118

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

N, W = map(int, input().split())
STP = [map(int, input().split()) for _ in range(N)]
S, T, P = [list(_) for _ in zip(*STP)]

print("Yes" if max(imos(S, T, P)) <= W else "No")
# %%
