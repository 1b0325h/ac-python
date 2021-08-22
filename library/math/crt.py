def extgcd(a, b):
    if not a:
        return (b, 0, 1)
    d, y, x = extgcd(b%a, a)
    return (d, x-b//a*y, y)


def crt(rem, mod):
    """
    >>> crt([1, 2], [2, 3])
    (5, 6)
    >>> crt([151, 57], [783, 278])
    (31471, 217674)
    """
    r, m = 0, 1
    for i in range(len(rem)):
        x, y, _ = extgcd(m, mod[i])
        if (a := rem[i]-r) % x:
            return (0, -1)
        r += m * (a//x*y % (mod[i]//x))
        m *= mod[i]//x
    return (r%m, m)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
