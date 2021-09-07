def base_n(n, base):
    """
    >>> base_n(11, 2)
    '1011'
    >>> base_n(1010101, 10)
    '1010101'
    >>> base_n(314159265, 3)
    '210220010221111100'
    """
    digit, s = 0, ""
    for i in range(10**9):
        if n < base**i:
            digit += i
            break
    for i in range(1, digit+1):
        s += str(x := n // (base**(digit-i)))
        n -= x * (base**(digit-i))
    return s



if __name__ == "__main__":
    import doctest
    doctest.testmod()
