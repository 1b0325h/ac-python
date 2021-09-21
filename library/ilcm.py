
def ilcm(x, y):
    """
    >>> ilcm(2, 3)
    6
    >>> ilcm(123, 456)
    18696
    >>> ilcm(100000, 99999)
    9999900000
    """
    u, v = x, y
    while y:
        x, y = y, x%y
    return u*v // x



if __name__ == "__main__":
    import doctest
    doctest.testmod()
