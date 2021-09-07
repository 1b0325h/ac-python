def rperm(p):
    """
    >>> rperm([2, 3, 1])
    [3, 1, 2]
    >>> rperm([5, 3, 2, 4, 1])
    [5, 3, 2, 4, 1]
    >>> rperm([6, 1, 3, 5, 4, 2])
    [2, 6, 3, 5, 4, 1]
    """
    p = [0]+p
    q = [-1]*len(p)
    for i in range(1, len(p)):
        q[p[i]] = i
    return q[1:]



if __name__ == "__main__":
    import doctest
    doctest.testmod()
