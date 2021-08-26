# https://atcoder.jp/contests/abc044/submissions/25327404

# %%
from collections import Counter

w = input()

for i in Counter(w).values():
    if i % 2:
        print("No")
        break
else:
    print("Yes")
# %%
