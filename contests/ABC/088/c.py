# https://atcoder.jp/contests/abc088/submissions/25530853

# %%
c = [list(map(int, input().split())) for _ in range(3)]

ans = "Yes"
if not c[0][0]-c[0][1] == c[1][0]-c[1][1] == c[2][0]-c[2][1]:
    ans = "No"
if not c[0][1]-c[0][2] == c[1][1]-c[1][2] == c[2][1]-c[2][2]:
    ans = "No"
if not c[0][0]-c[1][0] == c[0][1]-c[1][1] == c[0][2]-c[1][2]:
    ans = "No"
if not c[1][0]-c[2][0] == c[1][1]-c[2][1] == c[1][2]-c[2][2]:
    ans = "No"

print(ans)
# %%
