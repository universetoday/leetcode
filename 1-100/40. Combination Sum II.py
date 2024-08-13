"""
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
------------------------
Задача: дана коллекция чисел (candidates) и целевое число (target).
Необходимо найти все уникальные комбинации чисел из коллекции,
сумма которых равна целевому числу. Каждое число из коллекции
можно использовать в комбинации только один раз.

Важно: решение должно содержать только уникальные комбинации, то есть дубликаты не допускаются.
------------------------
MEDIUM
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start, path, target):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(i + 1, path + [candidates[i]], target - candidates[i])

        backtrack(0, [], target)
        return result


"""
Для решения задачи можно использовать метод поиска с возвратом (backtracking).
Объяснение:

    Сначала сортируем кандидатов, чтобы облегчить проверку дубликатов.
    Функция backtrack начинает с определенной позиции и проверяет все возможные комбинации, 
    используя оставшиеся числа.
    Если текущий кандидат уже встречался на данной позиции, он пропускается, чтобы избежать дубликатов.
    Если сумма равна целевому значению, комбинация добавляется в результат.
    Если сумма превышает целевую, дальнейшие комбинации не рассматриваются.
"""

candidates = [10,1,2,7,6,1,5]
target = 8
sol = Solution()
res = sol.combinationSum2(candidates, target)
print(res)
assert res == [
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

candidates = [2,5,2,1,2]
target = 5
sol = Solution()
res = sol.combinationSum2(candidates, target)
print(res)
assert res == [
[1,2,2],
[5]
]

