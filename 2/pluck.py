def pluck(data, path, default=None):
    res = data
    pas = path.split(".")
    while len(pas) > 0:
        res = res.setdefault(pas.pop(0), default)
    return res
