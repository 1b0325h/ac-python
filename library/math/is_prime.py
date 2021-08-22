def is_prime(n):
    """
    >>> is_prime(0)
    False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(73)
    True
    >>> is_prime(75)
    False
    >>> is_prime(-1)
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
