def primefactors(n):
    """
    >>> primefactors(42)
    [2, 3, 7]
    >>> primefactors(72)
    [2, 2, 2, 3, 3]
    >>> primefactors(147)
    [3, 7, 7]
    >>> primefactors(387)
    [3, 3, 43]
    """
    n = abs(n)
    x, i = [], 2
    while i*i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            x.append(i)
    if n > 1:
        x.append(n)
    return sorted(x)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
