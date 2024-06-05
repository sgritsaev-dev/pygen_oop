import sys
from collections import Counter

elems = Counter(el.strip() for el in sys.stdin)
total = 0
for key, value in elems.items():
    if value > 1:
        total += value - 1
print(total)
