# https://atcoder.jp/contests/past201912-open/submissions/25663849

# %%
N, Q = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(Q)]

graph = [["N"]*N for _ in range(N)]
for i in s:
    a = i[1]-1
    if i[0] == 1:
        graph[a][i[2]-1] = "Y"
    if i[0] == 2:
        for j in [i for i in range(N) if graph[i][a] == "Y"]:
            graph[a][j] = "Y"
    if i[0] == 3:
        for j in [i for i in range(N) if graph[a][i] == "Y"]:
            for k, u in enumerate(graph[j]):
                if u == "Y" and k != a:
                    graph[a][k] = "Y"

print(*["".join(i) for i in graph], sep="\n")
# %%
