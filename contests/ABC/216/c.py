# https://atcoder.jp/contests/abc216/submissions/25458276

# %%
N = int(input())

ans = ""
while N:
    if N % 2:
        N -= 1
        ans += "A"
    else:
        N //= 2
        ans += "B"

print(ans[::-1])
# %%
