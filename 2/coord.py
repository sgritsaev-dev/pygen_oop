import sys

for el in sys.stdin:
    x = eval(el.strip())
    print(-90 <= x[0] <= 90 and -180 <= x[1] <= 180)
