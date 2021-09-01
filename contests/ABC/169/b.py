# https://atcoder.jp/contests/abc169/submissions/25462796

# %%
N = int(input())
A = sorted(map(int, input().split()))

ans = 1
for i in A:
    ans *= i
    if ans > 10**18:
        print(-1)
        break
else:
    print(ans)
# %%
