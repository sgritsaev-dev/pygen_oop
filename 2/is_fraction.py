from fractions import Fraction


def is_fraction(string):
    try:
        int(string)
        return False
    except ValueError:
        pass
    try:
        float(string)
        return False
    except ValueError:
        pass
    try:
        Fraction(string)
        return True
    except Exception:
        return False
