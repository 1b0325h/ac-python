def prime_factors(n):
    """
    >>> prime_factors(42)
    [2, 3, 7]
    >>> prime_factors(72)
    [2, 2, 2, 3, 3]
    >>> prime_factors(147)
    [3, 7, 7]
    >>> prime_factors(387)
    [3, 3, 43]
    """
    table, i = [], 2
    while i*i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            table.append(i)
    if n > 1:
        table.append(n)
    return table



if __name__ == "__main__":
    import doctest
    doctest.testmod()
