# https://atcoder.jp/contests/abc149/submissions/25132259

# %%
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if not n % i:
            return False
    return True

X = int(input())

while not is_prime(X):
    X += 1

print(X)
# %%