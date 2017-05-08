def divisors(integer):
    """
    returns an array with all divisors of 'integer'
    (except for 1 and the number itself). 
    If the number is prime return '(integer) is prime' 
    """
    # Clever: return [i for i in xrange(2, integer) if not integer % i] or '%d is prime' % integer
    divisors = [x for x in xrange(2, integer) if integer % x == 0]
    if len(divisors) == 0:
        return '{} is prime'.format(integer)
    return divisors

"""
# Best practices
def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l
"""
