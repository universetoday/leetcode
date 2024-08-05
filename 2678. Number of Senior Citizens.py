"""You are given a 0-indexed array of strings details.
Each element of details provides information about a given passenger compressed into a string of length 15.
The system is such that:

    The first ten characters consist of the phone number of passengers.
    The next character denotes the gender of the person.
    The following two characters are used to indicate the age of the person.
    The last two characters determine the seat allotted to that person.

Return the number of passengers who are strictly more than 60 years old.
---------------------------------------

---------------------------------------
EASY
"""
from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for person in details:
            yearsold = int(person[-4:-2])
            if yearsold > 60:
                count += 1
        return count


details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
sol = Solution()
res = sol.countSeniors(details)
print(res)
assert res == 2

details = ["1313579440F2036","2921522980M5644"]
sol = Solution()
res = sol.countSeniors(details)
print(res)
assert res == 0

