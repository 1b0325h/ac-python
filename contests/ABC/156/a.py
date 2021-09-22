# https://atcoder.jp/contests/abc156/submissions/26037541

# %%
N, R = map(int, input().split())

if N >= 10:
    print(R)
else:
    print(R + 100*(10-N))
# %%
