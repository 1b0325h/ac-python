# https://atcoder.jp/contests/abc156/submissions/26037581

# %%
def base(n, b):
    r, s = 0, ""
    if b < 2:
        return None
    for i in range(10**9):
        if n < b**i:
            r += i
            break
    for i in range(1, r+1):
        s += str(x := n//(b**(r-i)))
        n -= x * (b**(r-i))
    return s

N, K = map(int, input().split())

print(len(base(N, K)))
# %%
