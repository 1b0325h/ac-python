# https://atcoder.jp/contests/abc043/submissions/25698882

# %%
s = input()

ans = ""
for i in s:
    if i == "0":
        ans += "0"
    if i == "1":
        ans += "1"
    if i == "B":
        ans = ans[:-1]

print(ans)
# %%
