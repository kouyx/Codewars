def f(n):
    """
    Add all the whole numbers 
    from 1 through a given number 'n'.

    Verify that 'n' is a valid positive integer number. 
    If not, return false (None for Python)
    """
    return sum([x for x in xrange(n + 1) if isinstance(n, int) and n > 0]) or None
