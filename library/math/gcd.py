def gcd(x, y):
    """
    >>> gcd(8, 9)
    1
    >>> gcd(30, 12)
    6
    """
    while y:
        x, y = y, x % y
    return x



if __name__ == "__main__":
    import doctest
    doctest.testmod()
