def f(n):
    """
    Add all the whole numbers 
    from 1 through a given number 'n'.

    Verify that 'n' is a valid positive integer number. 
    If not, return false (None for Python)
    """
    return sum(xrange(n + 1)) if (n > 0 and isinstance(n, int)) else None
