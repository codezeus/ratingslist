def is_float(value):
    """is_float determines if a value is a floating point number instance"""
    try:
        value = float(value)
        return True
    except ValueError:
        return False


def is_int(value):
    """is_int determines if a value is an integer instance"""
    try:
        value = int(value)
        return True
    except ValueError:
        return False


def is_numeric(value):
    """is_numeric determines if a value is an integer or float"""
    return is_int(value) or is_float(value)
