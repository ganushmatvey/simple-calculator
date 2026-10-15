"""Простой консольный калькулятор с обработкой ошибок ввода и деления на ноль."""


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


print("Самый лучший калькулятор.")
print("Если хотите выйти, введите 'q' в любом поле.")

while True:
    first_num = get_num("Введите первое число: ")
    if first_num == "q":
        break

    second_num = get_num("Введите второе число: ")
    if second_num == "q":
        break

    char = input("Введите операцию: ").strip()
    if char.lower() == "q":
        print("Выход из калькулятора.")
        break

    match char:
        case "+":
            print(f"Результат: {first_num + second_num}")
        case "-":
            print(f"Результат: {first_num - second_num}")
        case "*":
            print(f"Результат: {first_num * second_num}")
        case "/":
            try:
                print(f"Результат: {first_num / second_num}")
            except ZeroDivisionError:
                print("Деление на ноль недопустимо!")
        case "**":
            try:
                print(f"Результат: {first_num ** second_num}")
            except ZeroDivisionError:
                print("Деление на ноль недопустимо!")
        case _:
            print("Неизвестный оператор!")

    print("-" * 30)
