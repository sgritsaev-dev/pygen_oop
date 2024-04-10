import re
from collections import Counter

class TextHandler:
    def __init__(self) -> None:
        self.words_list = list()
        self.shortest_list = []
        self.longest_list = []

    def add_words(self, text):
        for el in re.findall(r'\b\w+\b', text):
            self.words_list.append(el)

    def get_shortest_words(self):
        if self.words_list:
            cnt = Counter(map(lambda x: len(x), self.words_list))
            shortest_amount = cnt[min(cnt)]
            self.shortest_list = list(sorted(self.words_list,key=lambda x: len(x)))[:shortest_amount]
        return self.shortest_list[:]

    def get_longest_words(self):
        if self.words_list:
            cnt = Counter(map(lambda x: len(x), self.words_list))
            longest_amount = cnt[max(cnt)]
            self.longest_list = list(
                sorted(self.words_list, key=lambda x: len(x)))[-longest_amount:]
        return self.longest_list[:]


texthandler = TextHandler()

texthandler.add_words('The world will hold my trial for your sins')
texthandler.add_words('Never meant to see the sky never meant to live')
print(list(sorted(texthandler.words_list, key=lambda x: len(x))))
print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())
