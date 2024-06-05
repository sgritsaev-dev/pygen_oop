def is_integer(string):
    for char in string[1:]:
        if char not in "1234567890":
            return False
    return True
