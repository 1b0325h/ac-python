# https://atcoder.jp/contests/abc127/submissions/25115635

# %%
A, B = map(int, input().split())

if A <= 5:
    print(0)
elif A <= 12:
    print(B//2)
else:
    print(B)
# %%
