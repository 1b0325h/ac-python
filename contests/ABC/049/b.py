# https://atcoder.jp/contests/abc049/submissions/25340195

# %%
H, W = map(int, input().split())
C = [input().split()*2 for _ in range(H)]

print(*sum(C, []), sep="\n")
# %%
