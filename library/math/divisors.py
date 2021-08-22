def divisors(n):
    """
    >>> divisors(4)
    [1, 2, 4]
    >>> divisors(5)
    [1, 5]
    >>> divisors(12)
    [1, 2, 3, 4, 6, 12]
    >>> divisors(30)
    [1, 2, 3, 5, 6, 10, 15, 30]
    """
    x, i = set(), 1
    while i**2 <= n:
        if not n % i:
            x.add(i)
            x.add(n//i)
        i += 1
    return sorted(x)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
