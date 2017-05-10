import re


def mix_fruit(arr):
    """
    Story
    Jumbo Juice makes a fresh juice out of fruits of your choice. 
    Jumbo Juice charges $5 for regular fruits and $7 for special ones. 
    
    Regular fruits are Banana, Orange, Apple, Lemon and Grapes. 
    Special ones are Avocado, Strawberry and Mango. 
    
    Others fruits that are not listed are also available upon request. 
    Those extra special fruits cost $9 per each. 
    There is no limit on how many fruits she/he picks.
    The price of a cup of juice is the mean of price of chosen fruits. 
    In case of decimal number (ex. $5.99), output should be the nearest integer (0.5 rounds up to 1).
    
    Input
    The function will receive an array of strings, each with the name of a fruit. 
    The recognition of names should be case insensitive.There is no case of an empty array input.
    """

    regular = re.compile(r'(Banana)|(Orange)|(Apple)|(Lemon)|(Grapes)', re.I)  # $5 per each
    special = re.compile(r'(Avocado)|(Strawberry)|(Mango)', re.I)  # $7 per each
    # return in 1 line if you wish:
    # return round(float(5 * len(regular.findall(','.join(arr))) + 7 * len(special.findall(','.join(arr))) + 9 * (len(arr) - len(regular.findall(','.join(arr))) - len(special.findall(','.join(arr))))) / len(arr))
    per_5 = len(regular.findall(','.join(arr)))
    per_7 = len(special.findall(','.join(arr)))
    return round(float(5 * per_5 + 7 * per_7 + 9 * (len(arr) - per_5 - per_7)) / len(arr))
