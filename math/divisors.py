def divisors(n) -> list:
   x = set()
   i = 1
   while i**2 <= n:
      if not n % i:
         x.add(i)
         x.add(n // i)
      i += 1
   return sorted(x)
