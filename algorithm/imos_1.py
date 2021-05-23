def imos_1(start: list, end: list, add: list) -> list:
   table = [0] * (x := max(end)+2)

   for i in range(len(start)):
      table[start[i]] += add[i]
      table[end[i]+1] -= add[i]

   for i in range(1, x):
      table[i] += table[i-1]

   return table
