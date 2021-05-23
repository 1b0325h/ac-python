def meguru(ng, ok) -> int:

   def _is_ok(mid) -> bool:
      # set the formula that returns a bool
      pass

   while abs(ok - ng) > 1:
      mid = (ok + ng) // 2
      if _is_ok(mid):
         ok = mid
      else:
         ng = mid
   return ok
