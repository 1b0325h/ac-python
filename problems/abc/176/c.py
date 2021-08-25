# https://atcoder.jp/contests/abc176/submissions/25115262

# %%
N = int(input())
A = list(map(int, input().split()))

ans = ret = 0
for i in A:
    ret = max(ret, i)
    ans += ret - i

print(ans)
# %%
