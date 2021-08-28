# https://atcoder.jp/contests/abc146/submissions/25136189

# %%
N = int(input())
S = input()

ans = ""
for i in S:
    ans += chr(65+(ord(i)-65+N) % 26)

print(ans)
# %%
