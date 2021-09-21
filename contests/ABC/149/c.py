# https://atcoder.jp/contests/abc149/submissions/26023709

# %%
def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if not n % i:
            return False
    return True

X = int(input())

while not isprime(X):
    X += 1

print(X)
# %%
