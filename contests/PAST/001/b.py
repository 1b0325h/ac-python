# https://atcoder.jp/contests/past201912-open/submissions/26024865

# %%
N = int(input())
A = [int(input()) for _ in range(N)]

ret = A[0]
for i in A[1:]:
    if ret == i:
        print("stay")
    if ret > i:
        print(f"down {ret-i}")
    if ret < i:
        print(f"up {i-ret}")
    ret = i
# %%
