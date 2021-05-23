def to_base_10(n: str, base: int) -> int:
   x = list(n)
   c = 0
   while x:
      c *= base
      c += int(x.pop(0))
   return c
