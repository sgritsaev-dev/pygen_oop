level = -1


class HtmlTag:
    def __init__(self, tag, inline=False):
        self.inline = inline
        self.start_tag = '<'+tag+'>'
        self.end_tag = '</'+tag+'>'

    def __enter__(self):
        global level
        level += 1
        if self.inline:
            print(('  ' * level)+self.start_tag, end='')
        else:
            print(('  ' * level)+self.start_tag)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        global level
        if self.inline:
            print(self.end_tag)
        else:
            print(('  ' * level)+self.end_tag)
        level -= 1

    def print(self, text):
        global level
        level += 1
        if self.inline:
            print(text, end='')
        else:
            print(('  ' * level)+text)
        level -= 1


with HtmlTag('body') as _:
    with HtmlTag('h1', True) as header:
        header.print('Поколение Python')
    with HtmlTag('p', True) as section:
        section.print(
            'Cерия курсов по языку программирования Python от команды BEEGEEK')
