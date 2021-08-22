# https://atcoder.jp/contests/abc183/submissions/25169397

# %%
def imos1(start, end, add):
    table = [0] * (max(end)+2)
    for i in range(len(start)):
        table[start[i]] += add[i]
        table[end[i]] -= add[i]
    for i in range(1, max(end)+2):
        table[i] += table[i-1]
    return table

N, W = map(int, input().split())
STP = [map(int, input().split()) for _ in range(N)]
S, T, P = [list(_) for _ in zip(*STP)]

print("Yes" if max(imos1(S, T, P)) <= W else "No")
# %%
