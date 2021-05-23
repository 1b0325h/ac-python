def ri(x, y) -> int:
   if x * y < 0:
      return int(x // y)
   else:
      return int((x + (-x % y)) / y)
