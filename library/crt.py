def crt(m, v):
    """
    >>> crt([783, 278], [151, 57])
    (31471, 217674)
    >>> crt([12, 6, 17], [3, 4, 2])
    (-1, 0)
    """
    r, u = 0, 1
    def _f(x, y):
        if not x:
            return (y, 0, 1)
        u, v, w = _f(y%x, x)
        return (u, w-y//x*v, v)
    for i in range(len(v)):
        x, y, _ = _f(u, m[i])
        if (w := v[i]-r) % x:
            return (-1, 0)
        r += u*(w//x*y%(m[i]//x))
        u *= m[i]//x
    return (r%u, u)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
