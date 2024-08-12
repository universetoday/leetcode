"""
You are given an integer array nums and an integer k.

In one operation,
you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
------------------------

------------------------
MEDIUM
"""
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        num_dict = {}

        for num in nums:
            complement = k - num  # вычисляем дополнение до k

            if complement in num_dict and num_dict[complement] > 0:
                # если дополнение есть в словаре и его количество больше 0, выполняем операцию
                count += 1
                num_dict[complement] -= 1
            else:
                # иначе добавляем текущее число в словарь
                if num in num_dict:
                    num_dict[num] += 1
                else:
                    num_dict[num] = 1

        return count


"""
Задача заключается в том, чтобы определить максимальное количество операций, 
которые можно выполнить на массиве, при этом в каждой операции выбираются два числа, 
сумма которых равна заданному числу k, 
и удаляются из массива. Необходимо вернуть количество таких операций.

Объяснение:

    Инициализация:
        count хранит количество возможных операций.
        num_dict — это словарь, который отслеживает количество оставшихся чисел в массиве.

    Проход по массиву:
        Для каждого числа num мы вычисляем его дополнение complement, такое что complement + num = k.
        Если complement уже есть в словаре и его количество больше 0, это значит, 
        что мы можем провести операцию — увеличить счетчик count и уменьшить количество complement 
        в словаре на 1.
        Если дополнение не найдено или его количество равно 0, 
        то текущее число добавляется в словарь или увеличивается его количество, если оно уже там есть.

    Возвращение результата:
        После прохода по массиву возвращаем значение count, 
        которое соответствует максимальному количеству операций.
"""

nums = [1,2,3,4]
k = 5
sol = Solution()
res = sol.maxOperations(nums, k)
print(res)
assert res == 2

nums = [3,1,3,4,3]
k = 6
sol = Solution()
res = sol.maxOperations(nums, k)
print(res)
assert res == 1
