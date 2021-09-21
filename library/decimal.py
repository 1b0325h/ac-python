def decimal(s, b):
    """
    >>> decimal("11", 2)
    3
    >>> decimal("13", 5)
    8
    >>> decimal("123", 8)
    83
    >>> decimal("1234", 10)
    1234
    """
    x, c = list(s), 0
    while x:
        c *= b
        c += int(x.pop(0))
    return c



if __name__ == "__main__":
    import doctest
    doctest.testmod()
