def to_base_n(n: int, base: int) -> str:
   digit = 0
   for i in range(10**9):
      if n < base**i:
         digit += i
         break
   s = ""
   for i in range(1, digit+1):
      s += str(x := n // (base**(digit-i)))
      n -= x * (base**(digit-i))
   return s
