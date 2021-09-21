def igcd(x, y):
    """
    >>> igcd(8, 9)
    1
    >>> igcd(30, 12)
    6
    """
    while y:
        x, y = y, x%y
    return x



if __name__ == "__main__":
    import doctest
    doctest.testmod()
