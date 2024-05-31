class Reloopable:
    def __init__(self, file) -> None:
        self.file = file

    def __enter__(self):
        return [el.strip() for el in self.file]

    def __exit__(self, *args, **kwargs):
        self.file.close()
        return True


with open("file.txt", "w") as file:
    file.write("Evil is evil\n")
    file.write("Lesser, greater, middling\n")
    file.write("Makes no difference\n")

with Reloopable(open("file.txt")) as reloopable:
    for line in reloopable:
        print(line.strip())
    for line in reloopable:
        print(line.strip())
