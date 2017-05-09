import re


def validate_pin(pin):
    """
    If 'pin' is a valid PIN string (containing exactly 4 or 6 digits), 
    return true, else return false.
    """
    return bool(re.match(r'^(\d{4}|\d{6})$', pin))


def validate_pin2(pin):
    return len(pin) in (4, 6) and pin.isdigit()
