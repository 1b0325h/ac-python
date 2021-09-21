def imos(start, end, add):
    """
    >>> N, W = 4, 10
    >>> S = [1, 2, 3, 2]
    >>> T = [3, 4, 10, 4]
    >>> P = [5, 4, 6, 1]
    >>> max(imos(S, T, P)) <= W
    False
    >>> N, W = 4, 10
    >>> S = [1, 2, 3, 2]
    >>> T = [3, 4, 10, 3]
    >>> P = [5, 4, 6, 1]
    >>> max(imos(S, T, P)) <= W
    True
    """
    table = [0] * (max(end)+2)
    for i in range(len(start)):
        table[start[i]] += add[i]
        table[end[i]] -= add[i]
    for i in range(1, max(end)+2):
        table[i] += table[i-1]
    return table



if __name__ == "__main__":
    import doctest
    doctest.testmod()
