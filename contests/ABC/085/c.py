# https://atcoder.jp/contests/abc085/submissions/25460874

# %%
N, Y = map(int, input().split())

ans = [-1] * 3
for x in range(N+1):
    for y in range(N-x+1):
        z = max(0, N-x-y)
        if x*10000 + y*5000 + z*1000 == Y:
            ans = [x, y, z]
            break

print(*ans)
# %%
