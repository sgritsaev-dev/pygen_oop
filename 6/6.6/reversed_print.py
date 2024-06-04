from contextlib import contextmanager
import sys


@contextmanager
def reversed_print():
    s = sys.stdout.write
    sys.stdout.write = lambda x: s(x[::-1])
    yield
    sys.stdout.write = s


with reversed_print():
    print("mazafaka")
