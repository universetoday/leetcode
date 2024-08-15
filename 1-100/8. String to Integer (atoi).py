"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

    Whitespace: Ignore any leading whitespace (" ").
    Signedness: Determine the sign by checking if the next character is '-' or '+',
    assuming positivity is neither present.
    Conversion: Read the integer by skipping leading zeros until a non-digit character
    is encountered or the end of the string is reached. If no digits were read, then the result is 0.
    Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1],
    then round the integer to remain in the range. Specifically,
    integers less than -231 should be rounded to -231,
    and integers greater than 231 - 1 should be rounded to 231 - 1.

Return the integer as the final result.
------------------------
Реализуйте функцию myAtoi(string s), которая преобразует строку в 32-битное целое число со знаком.

Алгоритм для myAtoi(string s) выглядит следующим образом:

    Пробельные символы: Игнорируйте любые начальные пробельные символы (" ").
    Знаковость: Определите знак, проверив, является ли следующий символ '-' или '+',
    предполагая, что знак не присутствует.
    Преобразование: Прочитайте целое число, пропуская ведущие нули,
    пока не будет встречен нецифровой символ или конец строки.
    Если цифры не были прочитаны, то результат будет 0.
    Округление: Если целое число выходит за пределы диапазона 32-битного целого числа со знаком [-231, 231 - 1],
    то округлите целое число, чтобы оно оставалось в этом диапазоне.
    Конкретно, целые числа меньше -231 должны быть округлены до -231,
    а целые числа больше 231 - 1 должны быть округлены до 231 - 1.

Верните целое число в качестве окончательного результата.
------------------------
MEDIUM
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. Удаление начальных пробельных символов
        s = s.lstrip()

        # Если строка пустая после удаления пробелов, верните 0
        if not s:
            return 0

        # 2. Определение знака
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # 3. Преобразование строки в число
        integer = 0
        for char in s:
            if char.isdigit():
                integer = integer * 10 + int(char)
            else:
                break

        # Применение знака к числу
        integer *= sign

        # 4. Округление до диапазона 32-битного целого числа со знаком
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1
        if integer < INT_MIN:
            return INT_MIN
        if integer > INT_MAX:
            return INT_MAX

        return integer


s = "42"
sol = Solution()
res = sol.myAtoi(s)
print(res)
assert res == 42

s = " -042"
sol = Solution()
res = sol.myAtoi(s)
print(res)
assert res == -42

s = "1337c0d3"
sol = Solution()
res = sol.myAtoi(s)
print(res)
assert res == 1337

s = "0-1"
sol = Solution()
res = sol.myAtoi(s)
print(res)
assert res == 0

s = "words and 987"
sol = Solution()
res = sol.myAtoi(s)
print(res)
assert res == 0

s = "-91283472332"
sol = Solution()
res = sol.myAtoi(s)
print(res)
assert res == -2147483648
