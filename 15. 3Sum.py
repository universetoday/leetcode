"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Для решения этой задачи можно использовать алгоритм:
        1. Отсортировать массив
        2. Пройти по массиву, используя текущий элемент как первый элемент тройки
        3. Использовать два указателя для поиска второго и третьего элемента тройки,
        чтобы сумма тройки равнялась нулю
        4. Ибегать дубликатов путем пропуска одинаковых элементов

        Этот алгоритм имеет временную сложность O(n^2) из-за двойного прохода по массиву
        """
        # Сортировка на месте
        nums.sort()
        result = []
        length = len(nums)
        for i in range(length - 2):
            # Пропускаем одинаковые элементы
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Указатели left и right, которые начинают поиск сразу после текущего и последнего элементов соответственно
            left = i + 1
            right = length - 1
            # Пока указатели не встретились, проверяем сумму трех элементов
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                # Еслм сумма отрицательная, то двигаем левый указатель вправо, чтобы увеличить сумму
                if s < 0:
                    left += 1
                # Если сумма положительная, то двигаем правы указатель влево, чобы уменьшить сумму
                elif s > 0:
                    right -= 1
                # Если сумма равна нулю, добавляем список найденных чисел к результирующему списку
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # Пока значения второго слева и следующего за ним чисел равны, двигаем указатель left вправо
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Пока значения второго справа и следующего перед ним чисел равны, двигаем указатель right влево
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result


nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
res = sol.threeSum(nums)
print(res)
assert res == [[-1, -1, 2], [-1, 0, 1]]

nums = [0, 1, 1]
sol = Solution()
res = sol.threeSum(nums)
print(res)
assert res == []

nums = [0, 0, 0]
sol = Solution()
res = sol.threeSum(nums)
print(res)
assert res == [[0, 0, 0]]