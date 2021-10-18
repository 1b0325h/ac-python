# https://atcoder.jp/contests/abc215/submissions/26663821

# %%
from itertools import permutations

S, K = input().split()

print(*sorted({*permutations(S)})[int(K)-1], sep="")
# %%
