def flatten(x: list):
   for i in x:
      if isinstance(i, list):
         yield from flatten(i)
      else:
         yield i
