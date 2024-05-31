class ReadableTextFile:
    def __init__(self, filename) -> None:
        self.filename = filename

    def __enter__(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            return [el.strip() for el in file.readlines()]

    def __exit__(self, *args, **kwargs):
        return True


with open("glados_quotes.txt", "w", encoding="utf-8") as file:
    print("Только посмотрите!", file=file)
    print("Как величаво она парит в воздухе", file=file)
    print("Как орел", file=file)
    print("На воздушном шаре", file=file)

with ReadableTextFile("glados_quotes.txt") as file:
    for line in file:
        print(line)
