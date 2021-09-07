# https://atcoder.jp/contests/abc217/submissions/25646036

# %%
def rperm(p):
    p = [0]+p
    q = [-1]*len(p)
    for i in range(1, len(p)):
        q[p[i]] = i
    return q[1:]

N = int(input())
p = list(map(int, input().split()))

print(*rperm(p))
# %%
