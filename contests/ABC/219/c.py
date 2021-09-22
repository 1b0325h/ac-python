# https://atcoder.jp/contests/abc219/submissions/26039111

# %%
from string import ascii_lowercase

X = str.maketrans(input(), ascii_lowercase)
N = int(input())
S = [input() for _ in range(N)]

print(*sorted(S, key=lambda s: s.translate(X)), sep="\n")
# %%
