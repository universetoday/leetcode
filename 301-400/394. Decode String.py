"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string],
where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid;
there are no extra white spaces, square brackets are well-formed, etc. Furthermore,
you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k. For example,
there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.
-------------------------------

-------------------------------
MEDIUM
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack_count = []
        stack_string = []
        current_string = ''
        current_count = 0

        for char in s:
            if char.isdigit():
                # Build the current repeat count number
                current_count = current_count * 10 + int(char)
            elif char == '[':
                # Push current string and count to stacks
                stack_string.append(current_string)
                stack_count.append(current_count)
                # Reset for new section
                current_string = ''
                current_count = 0
            elif char == ']':
                # Pop count and previous string
                prev_string = stack_string.pop()
                repeat_count = stack_count.pop()
                # Decode current string
                current_string = prev_string + (current_string * repeat_count)
            else:
                # Build current string
                current_string += char

        return current_string


"""
Дана закодированная строка, верните ее раскодированную версию.

Правило кодирования таково: k[encoded_string], 
где строка encoded_string внутри квадратных скобок повторяется ровно k раз. 
Обратите внимание, что k гарантированно является положительным целым числом.

Вы можете предположить, что входная строка всегда корректна; 
нет лишних пробелов, квадратные скобки оформлены правильно и т. д. Более того, 
вы можете предположить, что исходные данные не содержат цифр, 
а цифры предназначены только для повторяющихся чисел k. Например, не будет ввода вроде 3a или 2[4].

Тестовые случаи сгенерированы так, чтобы длина вывода никогда не превышала 105.
"""


s = "3[a]2[bc]"
sol = Solution()
res = sol.decodeString(s)
print(res)
assert res == "aaabcbc"

s = "3[a2[c]]"
sol = Solution()
res = sol.decodeString(s)
print(res)
assert res == "accaccacc"

s = "2[abc]3[cd]ef"
sol = Solution()
res = sol.decodeString(s)
print(res)
assert res == "abcabccdcdcdef"
