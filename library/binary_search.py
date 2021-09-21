def binary_search(ok, ng, f):
    """
    >>> arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    >>> target = 64
    >>> binary_search(len(arr), -1, lambda x: arr[x] >= target)
    6
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
