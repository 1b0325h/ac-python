# https://atcoder.jp/contests/abc127/submissions/25169324

# %%
def imos1(start, end, add):
    table = [0] * (max(end)+2)
    for i in range(len(start)):
        table[start[i]] += add[i]
        table[end[i]] -= add[i]
    for i in range(1, max(end)+2):
        table[i] += table[i-1]
    return table

N, M = map(int, input().split())
LR = [map(int, input().split()) for _ in range(M)]
L, R = [list(_) for _ in zip(*LR)]

print(imos1(L, [i+1 for i in R], [1]*M).count(M))
# %%
