# https://atcoder.jp/contests/abc212/submissions/25307950

# %%
X = input()

if len(set(X)) == 1:
    print("Weak")
elif all(int(X[i+1]) == (int(X[i])+1) % 10 for i in range(3)):
    print("Weak")
else:
    print("Strong")
# %%
