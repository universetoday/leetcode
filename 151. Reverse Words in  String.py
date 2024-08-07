"""Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.
---------------------------------------
Дана строка s. Переверни порядок строк.

Слово определяется как последовательность символов без пробелов.
Слова в строке будут отделяться по крайней мере одним пробелом.

Возврати строку из слов в перевернутом порядке с одним пробелом.

Отметь, что строка может содержать пробел перед словом или после строки или несколько пробелов.
---------------------------------------
MEDIUM
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        list_s = s.split()
        left = 0
        right = len(list_s)-1
        while left < right:
            if list_s[left] == ' ':
                del list_s[left]
            if list_s[right] == ' ':
                del list_s[right]
            if list_s[left] != ' ' and list_s[right] != ' ':
                list_s[left], list_s[right] = list_s[right], list_s[left]
                left += 1
                right -= 1
        return ' '.join(list_s)


s = "the sky is blue"
sol = Solution()
res = sol.reverseWords(s)
print(res)
assert res == "blue is sky the"

s = "  hello world  "
sol = Solution()
res = sol.reverseWords(s)
print(res)
assert res == "world hello"

s = "a good   example"
sol = Solution()
res = sol.reverseWords(s)
print(res)
assert res == "example good a"
