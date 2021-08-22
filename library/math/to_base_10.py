def to_base_10(n, base):
    """
    >>> to_base_10("11", 2)
    3
    >>> to_base_10("13", 5)
    8
    >>> to_base_10("123", 8)
    83
    >>> to_base_10("1234", 10)
    1234
    """
    x, c = list(n), 0
    while x:
        c *= base
        c += int(x.pop(0))
    return c



if __name__ == "__main__":
    import doctest
    doctest.testmod()
