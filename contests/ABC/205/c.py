# https://atcoder.jp/contests/abc205/submissions/26040807

# %%
A, B, C = map(int, input().split())

C = 1 if C % 2 else 2
A = pow(A, C)
B = pow(B, C)

if A < B:
    print("<")
elif A > B:
    print(">")
else:
    print("=")
# %%
