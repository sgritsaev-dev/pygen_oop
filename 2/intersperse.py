def intersperse(iterable, delimeter):
    if hasattr(iterable, "__next__"):
        try:
            yield next(iterable)
            for el in iterable:
                yield delimeter
                yield el
        except:
            pass
    else:
        try:
            yield iterable[0]
            for el in iterable[1:]:
                yield delimeter
                yield el
        except:
            pass


iterable = iter("")

print(*intersperse(iterable, "+"))
