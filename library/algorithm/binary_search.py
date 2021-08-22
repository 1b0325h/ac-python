def binary_search(ng, ok, f):
    """
    >>> def f(mid):
    ...     return A*mid + B*len(str(mid)) <= X
    >>> A, B, X = 10, 7, 100
    >>> binary_search(10**9 + 1, 0, f)
    9
    >>> A, B, X = 2, 1, 10**11
    >>> binary_search(10**9 + 1, 0, f)
    1000000000
    >>> A, B, X = 10**9, 10**9, 100
    >>> binary_search(10**9 + 1, 0, f)
    0
    >>> A, B, X = 1234, 56789, 314159265
    >>> binary_search(10**9 + 1, 0, f)
    254309
    """
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    return ok



if __name__ == "__main__":
    import doctest
    doctest.testmod()
