# https://atcoder.jp/contests/abc081/submissions/25132705

# %%
N = int(input())
A = list(map(int, input().split()))

ans = 0
while all(not i % 2 for i in A):
    A = [i//2 for i in A]
    ans += 1

print(ans)
# %%
