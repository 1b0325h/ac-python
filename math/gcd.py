def gcd(x, y):
   if not y:
      return x
   while y:
      x, y = y, x % y
   return x
