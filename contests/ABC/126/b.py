# https://atcoder.jp/contests/abc126/submissions/25500173

# %%
S = input()

A, B = map(int, [S[:2], S[2:]])
if 0 < A < 13:
    if 0 < B < 13:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if 0 < B < 13:
        print("YYMM")
    else:
        print("NA")
# %%
