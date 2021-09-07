# https://atcoder.jp/contests/past202005-open/submissions/25661008

# %%
N, M, Q = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(Q)]

for i in s:
    x = i[1] - 1
    print(c[x])
    if i[0] == 1:
        for j in graph[x]:
            c[j] = c[x]
    if i[0] == 2:
        c[x] = i[2]
# %%
