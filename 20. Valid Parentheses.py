"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

------------------------
Чтобы определить, является ли строка s, содержащая только символы '(', ')', '{', '}', '[' и ']',
допустимой, нужно проверить следующее:

    Открывающие скобки должны быть закрыты скобками того же типа.
    Открывающие скобки должны быть закрыты в правильном порядке.
    Каждая закрывающая скобка должна иметь соответствующую открывающую скобку того же типа.
------------------------
Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

------------------------
EASY
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # Создаем словарь для хранения пар скобок
        brackets = {')': '(', '}': '{', ']': '['}
        # Пустой список для обработки строки
        stack = []
        for char in s:
            if char in brackets:
                # Берем верхний элемент stack
                top_element = stack.pop() if stack else '#'
                # Проверяем, соответствует ли он открывающей скобке из словаря
                if brackets[char] != top_element:
                    return False
            else:
                # Если символ является открывающей скобкой, то добавляем ее в stack
                stack.append(char)
        # Если стек пуст после обработки всей строки, значит все скобки сбалансированы
        return not stack



s = "()"
sol = Solution()
res = sol.isValid(s)
print(res)
assert res == True

s = "()[]{}"
sol = Solution()
res = sol.isValid(s)
print(res)
assert res == True

s = "(]"
sol = Solution()
res = sol.isValid(s)
print(res)
assert res == False