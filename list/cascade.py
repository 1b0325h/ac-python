def cascade(x:list, n:int):
   for i in range(len(x)-n+1):
      yield x[i:i+n]
