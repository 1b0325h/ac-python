# https://atcoder.jp/contests/abc042/submissions/25463151

# %%
N, K = map(int, input().split())
D = input().split()

while True:
    for i in str(N):
        if i in D:
            N += 1
            break
    else:
        break

print(N)
# %%
