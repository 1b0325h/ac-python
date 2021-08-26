# https://atcoder.jp/contests/abc045/submissions/25328553

# %%
A, B, C = [list(input().upper()) for _ in range(3)]
S = {"A": A, "B": B, "C": C}

ans = "A"
while S[ans]:
    ans = S[ans].pop(0)

print(ans)
# %%
