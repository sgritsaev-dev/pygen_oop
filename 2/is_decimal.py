def is_decimal(string):
    if (len(string) == 1 and string not in "1234567890") or len(string) == 0:
        return False
    if string.count(".") > 1:
        return False
    for char in string[1:]:
        if char not in "1234567890.":
            return False
    return True


print(is_decimal("a"))
