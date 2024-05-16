class Calculator:
    def __call__(self, arg1, arg2, operation):
        match operation:
            case "+":
                return arg1 + arg2
            case "-":
                return arg1 - arg2
            case "*":
                return arg1 * arg2
            case "/":
                try:
                    return arg1 / arg2
                except ZeroDivisionError:
                    raise ValueError("Деление на ноль невозможно")


calculator = Calculator()

try:
    print(calculator(10, 0, "/"))
except ValueError as e:
    print(e)
    print(type(e))
