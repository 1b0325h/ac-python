# https://atcoder.jp/contests/abc192/submissions/25150068

# %%
S = input()

ans = []
for i, s in enumerate(S):
    if i % 2:
        ans.append(s.isupper())
    else:
        ans.append(s.islower())

print(["No", "Yes"][all(ans)])
# %%
