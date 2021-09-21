def base(n, b):
    """
    >>> base(11, 2)
    '1011'
    >>> base(1010101, 10)
    '1010101'
    >>> base(314159265, 3)
    '210220010221111100'
    """
    r, s = 0, ""
    if b < 2:
        return None
    for i in range(10**9):
        if n < b**i:
            r += i
            break
    for i in range(1, r+1):
        s += str(x := n//(b**(r-i)))
        n -= x * (b**(r-i))
    return s



if __name__ == "__main__":
    import doctest
    doctest.testmod()
