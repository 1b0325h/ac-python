# https://atcoder.jp/contests/abc186/submissions/25291986

# %%
H, W = map(int, input().split())
A = [x for _ in range(H) for x in map(int, input().split())]

print(sum(A) - min(A)*H*W)
# %%
