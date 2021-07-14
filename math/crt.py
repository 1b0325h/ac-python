def crt(rem: list, mod: list) -> tuple:
   def _egcd(a, b):
      if not a:
         return (b, 0, 1)
      else:
         d, y, x = _egcd(b % a, a)
         return (d, x - b//a * y, y)

   r, m = 0, 1
   for i in range(len(rem)):
      x, y, _ = _egcd(m, mod[i])
      if (a := rem[i]-r) % x:
         return (0, -1)
      r += m * (a // x*y % (mod[i]//x))
      m *= mod[i]//x

   return (r % m, m)
