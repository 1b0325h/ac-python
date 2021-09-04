# https://atcoder.jp/contests/abc165/submissions/25532105

# %%
K = int(input())
A, B = map(int, input().split())

for i in range(A, B+1):
    if not i % K:
        print("OK")
        break
else:
    print("NG")
# %%
