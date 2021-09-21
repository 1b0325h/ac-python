def isprime(n):
    """
    >>> isprime(0)
    False
    >>> isprime(1)
    False
    >>> isprime(2)
    True
    >>> isprime(73)
    True
    >>> isprime(75)
    False
    >>> isprime(-1)
    False
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if not n % i:
            return False
    return True



if __name__ == "__main__":
    import doctest
    doctest.testmod()
