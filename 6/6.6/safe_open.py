from contextlib import contextmanager


@contextmanager
def safe_open(filename, mode="r"):
    try:
        f = open(filename, mode)
        yield (f, None)
        f.close()
    except Exception as err:
        yield (None, err)
