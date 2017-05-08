def divisors(integer):
    """
    returns an array with all divisors of 'integer'
    (except for 1 and the number itself). 
    If the number is prime return '(integer) is prime' 
    """
    a = []
    for x in range(2, integer):
        if integer % x == 0:
            a.append(x)
    if not a:
        return '{} is prime'.format(integer)
    else:
        return a