# https://atcoder.jp/contests/abc148/submissions/25163730

# %%
N = int(input())
S, T = input().split()

print("".join(S[i] + T[i] for i in range(N)))
# %%
