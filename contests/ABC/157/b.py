# https://atcoder.jp/contests/abc157/submissions/25515249

# %%
A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
b = [int(input()) for _ in range(N)]

for i in range(3):
    for j in range(3):
        for k in b:
            if A[i][j] == k:
                A[i][j] = 0

ans = "No"
for i in range(3):
    if not A[0][i]+A[1][i]+A[2][i]:
        ans = "Yes"
    if not A[i][0]+A[i][1]+A[i][2]:
        ans = "Yes"
if not A[0][0]+A[1][1]+A[2][2]:
    ans = "Yes"
if not A[2][0]+A[1][1]+A[0][2]:
    ans = "Yes"

print(ans)
# %%
