# https://atcoder.jp/contests/past202005-open/submissions/25513545

# %%
s = input()
t = input()

if s == t:
    print("same")
elif s.lower() == t.lower():
    print("case-insensitive")
else:
    print("different")
# %%
