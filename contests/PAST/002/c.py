# https://atcoder.jp/contests/past202004-open/submissions/25513390

# %%
N = int(input())
S = [list(input()) for _ in range(N)]

for i in range(N-2, -1, -1):
    for j in range(2*N-1):
        if S[i][j] == "#":
            if S[i+1][j-1] == "X":
                S[i][j] = "X"
            elif S[i+1][j] == "X":
                S[i][j] = "X"
            elif S[i+1][j+1] == "X":
                S[i][j] = "X"

print(*["".join(i) for i in S], sep="\n")
# %%
