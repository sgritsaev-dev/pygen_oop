import re


class StrExtension:
    @staticmethod
    def remove_vowels(string):
        for char in re.findall(r'[aeiouy]', string, flags=re.IGNORECASE):
            string = string.replace(char, '')
        return string

    @staticmethod
    def leave_alpha(string):
        for char in re.findall(r'\W|\d', string, flags=re.IGNORECASE):
            string = string.replace(char, '')
        return string

    @staticmethod
    def replace_all(string, chars, char):
        for el in chars:
            string = string.replace(el, char)
        return string


print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))
