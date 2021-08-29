# https://atcoder.jp/contests/abc123/submissions/25326117

# %%
A = [int(input()) for _ in range(5)]

ans = ret = 0
for i in A:
    if x := (10-i)%10:
        ans += x
    ans += i
    ret = max(ret, x)

print(ans-ret)
# %%
