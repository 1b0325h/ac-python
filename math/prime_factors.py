def prime_factors(n: int) -> list:
   table, f = [], 3
   while not n % 2:
      n //= 2
      table.append(2)
   while f*f <= n:
      if not n % f:
         n //= f
         table.append(f)
      else:
         f += 2
   if n != 1:
      table.append(n)
   return table
