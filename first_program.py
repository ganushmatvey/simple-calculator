"""Простой консольный калькулятор с обработкой ошибок ввода и деления на ноль."""

print("Калькулятор на Python.")

while True:
    try:
        first_input = input("Введите первое число (или 'q' для выхода): ")

        if first_input.lower() == "q":
            print("Выход из калькулятора.")
            break

        first_num = float(first_input)
        second_num = float(input("Введите второе число: "))

        char = input("Введите операцию: ")

        if char == "+":
            print(f"Результат: {first_num + second_num}")
        elif char == "-":
            print(f"Результат: {first_num - second_num}")
        elif char == "*":
            print(f"Результат: {first_num * second_num}")
        elif char == "/":
            print(f"Результат: {first_num / second_num}")
        else:
            print("Не понял ваш оператор")

    except ValueError:
        print("Вы ввели не число!")
    except ZeroDivisionError:
        print("Деление на ноль недопустимо!")
