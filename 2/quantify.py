def quantify(seq, func):
    return len(list(filter(func, seq)))
