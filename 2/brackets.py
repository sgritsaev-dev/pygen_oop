def checker(brackets):
    total = 0
    for el in brackets:
        if el == "(":
            total += 1
        elif el == ")":
            total -= 1
        if total < 0:
            return False
    if total != 0:
        return False
    return True


print(checker(input()))
