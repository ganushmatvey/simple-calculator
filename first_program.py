import operator

OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "**": operator.pow,
}


def get_num(prompt):
    """Функция безопасного ввода числа с возможностью выхода."""
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == "q":
            print("Выход из калькулятора.")
            return "q"
        try:
            return float(user_input)
        except ValueError:
            print("Вы ввели не число, попробуйте еще раз!")


print("Калькулятор на Python.")
print("Если хотите выйти, введите 'q' в любом поле.")

while True:
    first_num = get_num("Введите первое число: ")
    if first_num == "q":
        break

    second_num = get_num("Введите второе число: ")
    if second_num == "q":
        break

    char = input(f"Введите операцию ({', '.join(OPERATIONS.keys())}): ").strip()

    if char.lower() == "q":
        print("Выход из калькулятора.")
        break

    if char in OPERATIONS:

        calc_function = OPERATIONS[char]

        try:
            result = calc_function(first_num, second_num)
            print(f"Результат: {result}")
        except ZeroDivisionError:
            print("Ошибка! Деление на ноль недопустимо")

    else:
        print("Неизвестный оператор")

    print("-" * 30)
