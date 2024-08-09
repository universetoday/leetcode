"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

    If the group's length is 1, append the character to s.
    Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.
---------------

---------------
MEDIUM
"""
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        count = 1
        res = []
        for i in range(1, len(chars)):
            if chars[i-1] == chars[i]:
                count += 1
            else:
                res.append(chars[i-1])
                if count > 1:
                    res.extend(list(str(count)))
                count = 1

        # Добавляем последний символ и его количество
        res.append(chars[-1])
        if count > 1:
            res.extend(list(str(count)))

        # Изменяем исходный список chars
        chars[:len(res)] = res
        return len(res)


chars = ["a","a","b","b","c","c","c"]
sol = Solution()
res = sol.compress(chars)
print(res)
assert res == 6

chars = ["a"]
sol = Solution()
res = sol.compress(chars)
print(res)
assert res == 1

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
sol = Solution()
res = sol.compress(chars)
print(res)
assert res == 4
