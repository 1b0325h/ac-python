# https://atcoder.jp/contests/past201912-open/submissions/25512196

# %%
N = int(input())
A = [int(input()) for _ in range(N)]

ret = A[0]
for i in A[1:]:
    if ret == i:
        print("stay")
    elif ret > i:
        print(f"down {ret-i}")
    else:
        print(f"up {i-ret}")
    ret = i
# %%
