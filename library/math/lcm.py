def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    """
    >>> lcm(2, 3)
    6
    >>> lcm(123, 456)
    18696
    >>> lcm(100000, 99999)
    9999900000
    """
    return x * y // gcd(x, y)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
