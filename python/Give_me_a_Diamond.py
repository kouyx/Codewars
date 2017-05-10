def diamond(n):
    """
    the number 'n' represents the number of '*'s printed on the middle line.
    The line above and below will be centered and will have 2 less '*'s than the middle line. 
    This reduction by 2 '*'s for each line continues 
    until a line with a single * is printed at the top and bottom of the figure.
    
    return None for invalid input (even number or negative)
    expected =  " *\n"
    expected += "***\n"
    expected += " *\n"
    """
    # Make some diamonds!
    if n % 2 == 0 or n < 0:
        return None
    return ''.join("{}{}\n".format((' ' * ((n - x) / 2)), '*' * x) for x in (range(1, n, 2) + range(n, 0, -2)))
