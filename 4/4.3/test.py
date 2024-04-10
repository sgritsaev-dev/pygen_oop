from collections import Counter

test = ['my', 'to', 'to', 'The', 'for', 'see', 'the', 'sky', 'will', 'hold', 'your', 'sins', 'live', 'world', 'trial', 'Never', 'meant', 'never', 'meant']

cnt = Counter(map(lambda x: len(x), test))
print(cnt[min(cnt)], cnt[max(cnt)])