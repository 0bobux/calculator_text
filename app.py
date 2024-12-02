def calc(expression):
    """
    Калькулятор, который переводит текст в числа, считает их, переводит результат в текст и возвращает этот текст.

    :param expression: string
    :return: string
    """
    ones = {
        "ноль": 0, "один": 1,"одна": 1,"две": 2, "два": 2, "три": 3, "четыре": 4,
        "пять": 5, "шесть": 6, "семь": 7, "восемь": 8, "девять": 9
    }
    teens = {
        "десять": 10, "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13,
        "четырнадцать": 14, "пятнадцать": 15, "шестнадцать": 16,
        "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19
    }
    tens = {
        "двадцать": 20, "тридцать": 30, "сорок": 40, "пятьдесят": 50,
        "шестьдесят": 60, "семьдесят": 70, "восемьдесят": 80, "девяносто": 90
    }
    hundreds = {
        "сто": 100, "двести": 200, "триста": 300, "четыреста": 400, "пятьсот": 500,
        "шестьсот": 600, "семьсот": 700, "восемьсот": 800, "девятьсот": 900
    }
    operations = {
        "плюс": "+", "минус": "-", "умножить на": "*",
        "разделить на": "/", "остаток от деления на": "%"
    }
    fractional_type = ["сотых", "десятых", "тысячных"]

    def to_number(text):
        """
        Функция принимает текст и переводит его в число.

        :param text: string
        :return: int/float
        """
        if " и " in text:
            integer_part, fractional_part = text.split(" и ")
            integer_value = to_number(integer_part)
            fractional_value = to_number_fraction(fractional_part)
            return integer_value + fractional_value
        parts = text.split()
        number = 0
        if len(parts) == 1:
            if parts[0] in ones:
                number += ones[parts[0]]
            elif parts[0] in teens:
                number += teens[parts[0]]
            elif parts[0] in tens:
                number += tens[parts[0]]
            else:
                raise ValueError("Неверный ввод / не найдена цифра.")
        elif len(parts) == 2:
            if parts[0] in tens and parts[1] in ones:
                number = tens[parts[0]] + ones[parts[1]]
            else:
                raise ValueError("Неверный ввод / не найдена цифра.")
        return number

    def to_number_fraction(text):
        """
        Функция преобразовывает текст в число типа float.

        :param text: string
        :return: float
        """
        parts = text.split()
        number = 0
        if len(parts) == 1:
            if parts[0] in ones:
                number += ones[parts[0]] / 10
            elif parts[0] in teens:
                number += teens[parts[0]] / 100
            elif parts[0] in tens:
                number += tens[parts[0]] / 100
            elif parts[0] in hundreds:
                number += hundreds[parts[0]] / 1000
        elif len(parts) == 2:
            if parts[0] in tens and parts[1] in ones:
                number = (tens[parts[0]] + ones[parts[1]]) / 100
        elif len(parts) == 2:
            if parts[0] in hundreds and parts[1] in ones:
                number = (hundreds[parts[0]] + ones[parts[1]]) / 1000
        elif len(parts) == 2:
            if parts[0] in hundreds and parts[1] in teens:
                number = (hundreds[parts[0]] + teens[parts[1]]) / 1000
        elif len(parts) == 2:
            if parts[0] in hundreds and parts[1] in tens:
                number = (hundreds[parts[0]] + tens[parts[1]]) / 1000
        elif len(parts) == 3:
            if parts[0] in hundreds and parts[1] in tens and parts[2] in ones:
                number = (hundreds[parts[0]] + tens[parts[1]] + ones[parts[2]]) / 1000
        return number

    def to_text(number):
        """
        Функция преобразовывает числа типов int/float в текст.

        :param number: int/float
        :return: string
        """
        if isinstance(number, float) and number.is_integer():
            number = int(number)

        if isinstance(number, int):
            ones_text = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
            teens_text = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
                          "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
            tens_text = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
                         "девяносто"]
            hundreds_text = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот",
                             "девятьсот"]
            thousands_text = ["", "одна тысяча", "две тысячи", "три тысячи", "четыре тысячи", "пять тысяч",
                              "шесть тысяч", "семь тысяч", "восемь тысяч", "девять тысяч"]

            result = ""
            if number >= 1000:
                thousands = number // 1000
                result += thousands_text[thousands]
                number %= 1000
                if number > 0:
                    result += " "

            if number >= 100:
                hundreds = number // 100
                result += hundreds_text[hundreds]
                number %= 100
                if number > 0:
                    result += " "

            if number >= 20:
                tens = number // 10
                result += tens_text[tens]
                number %= 10
                if number > 0:
                    result += " "

            if number >= 10:
                result += teens_text[number - 10]
            elif number > 0:
                result += ones_text[number]

            return result.strip()

        else:
            # Для дробных чисел
            integer_part, fractional_part = divmod(number, 1)
            fractional_part2 = round(fractional_part, 3)
            fractional_part1 = str(fractional_part2).split(".")
            integer_part = int(integer_part)
            fractional_part = int(fractional_part1[1])
            if len(str(fractional_part)) == 3:
                frac_type = " тысячных"
            elif len(str(fractional_part)) == 2:
                frac_type = " сотых"
            elif len(str(fractional_part)) == 1:
                frac_type = " десятых"
            ones_text = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
            teens_text = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
                          "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
            tens_text = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
                         "девяносто"]
            hundreds_text = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот",
                             "девятьсот"]
            thousands_text = ["", "одна тысяча", "две тысячи", "три тысячи", "четыре тысячи", "пять тысяч",
                              "шесть тысяч", "семь тысяч", "восемь тысяч", "девять тысяч"]
            result = ""
            if integer_part >= 1000:
                thousands = integer_part // 1000
                result += thousands_text[thousands]
                integer_part %= 1000
                if integer_part > 0:
                    result += " "

            if integer_part >= 100:
                hundreds = integer_part // 100
                result += hundreds_text[hundreds]
                integer_part %= 100
                if integer_part > 0:
                    result += " "

            if integer_part >= 20:
                tens = integer_part // 10
                result += tens_text[tens]
                integer_part %= 10
                if integer_part > 0:
                    result += " "

            if integer_part >= 10:
                result += teens_text[integer_part - 10]
            elif integer_part >= 0:
                result += ones_text[integer_part]

            result += " и "

            if fractional_part >= 1000:
                thousands = fractional_part // 1000
                result += thousands_text[thousands]
                fractional_part %= 1000
                if fractional_part > 0:
                    result += " "

            if fractional_part >= 100:
                hundreds = fractional_part // 100
                result += hundreds_text[hundreds]
                fractional_part %= 100
                if fractional_part > 0:
                    result += " "

            if fractional_part >= 20:
                tens = fractional_part // 10
                result += tens_text[tens]
                fractional_part %= 10
                if fractional_part > 0:
                    result += " "

            if fractional_part >= 10:
                result += teens_text[fractional_part - 10]
            elif fractional_part > 0:
                result += ones_text[fractional_part]

            result += frac_type

            return result.strip()


    for op in operations:
        if f" {op} " in expression:
            left_text1, right_text1 = expression.split(f" {op} ")
            operation = operations[op]
            break
    else:
        raise ValueError("Не удалось найти арифметическую операцию в строке.")

    #Удаляем слова "сотых","десятых","тысячных"
    left_text = ' '.join(word for word in left_text1.split() if word not in fractional_type)
    right_text = ' '.join(word for word in right_text1.split() if word not in fractional_type)

    left_number = to_number(left_text)
    right_number = to_number(right_text)

    if operation == "+":
        result = left_number + right_number
    elif operation == "-":
        result = left_number - right_number
    elif operation == "*":
        result = left_number * right_number
    elif operation == "/":
        if right_number == 0:
            raise ValueError("Деление на ноль невозможно.")
        result = left_number / right_number
    elif operation == "%":
        if right_number == 0:
            raise ValueError("Остаток от деления на ноль невозможен.")
        result = left_number % right_number
    else:
        raise ValueError(f"Неизвестная операция: {operation}")

    return to_text(result)

# Примеры:
print(calc("сорок один и тридцать один сотых разделить на семнадцать"))
print(calc("девяносто девять умножить на девяносто девять"))
print(calc("пять минус один"))
print(calc("семьдесят восемь плюс два"))
print(calc("двадцать три остаток от деления на десять"))
print(calc("девятнадцать и восемьдесят две сотых разделить на девяносто девять"))
#print(calc("два три плюс четыре"))
#print(calc("сто плюс один"))
#print(calc("минус два три"))
#print(calc("минус два плюс три"))