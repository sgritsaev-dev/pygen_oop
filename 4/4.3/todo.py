class Todo:
    def __init__(self) -> None:
        self.things = list()
        self.hp = 0
        self.lp = 0
    def add(self, name, priority):
        self.things.append(tuple([name, priority]))
        self.hp = max(map(lambda x: x[1], self.things))
        self.lp = min(map(lambda x: x[1], self.things))
    def get_by_priority(self, n):
        return [el[0] for el in self.things if el[1]==n]

    def get_low_priority(self):
        return [el[0] for el in self.things if el[1]==self.lp]

    def get_high_priority(self):
        return [el[0] for el in self.things if el[1]==self.hp]

todo = Todo()

todo.add('Ответить на вопросы', 5)
todo.add('Сделать картинки', 1)
todo.add('Доделать задачи', 4)
todo.add('Дописать конспект', 5)

print(todo.get_low_priority())
print(todo.get_high_priority())
print(todo.get_by_priority(3))