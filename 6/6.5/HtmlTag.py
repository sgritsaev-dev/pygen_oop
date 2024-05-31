class HtmlTag:
    
    def __init__(self, tag, inline=False):
        self.inline = inline
        self.start_tag = '<'+tag+'>'
        self.end_tag = '</'+tag+'>'

    def __enter__(self):
        self.level += 1
        if self.inline:
            print(('  ' * self.level)+self.start_tag)
        else:
            print(('  ' * self.level)+self.start_tag)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(self.end_tag)
        self.level -= 1

    def print(self, text):
        self.level+=1
        print(('  ' * self.level)+text)
            
with HtmlTag('table') as _:
    with HtmlTag('tr') as paragraph:
        with HtmlTag('th', True) as field:
            field.print('текст заголовка')
        with HtmlTag('td') as data:
            with HtmlTag('ul'):
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')