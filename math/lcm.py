def lcm(x, y):
   if not y:
      return 0
   def _gcd(x, y):
      while y:
         x, y = y, x % y
      return x
   return x * y // _gcd(x, y)
