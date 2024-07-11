

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 1. инициализируем пустой словарь
        num_to_index = {}
        # 2. Итерация: Проходимся по списку чисел, используя enumerate, чтобы получить индекс i и значение num каждого элемента
        for i, num in enumerate(nums):
            # 3. Вычисление дополнительного числа target - num
            complement = target - num
            # 4. Проверка наличия дополнительного числа complement в словаре
            print(complement)
            print(num_to_index)
            if complement in num_to_index:
                # Если в словаре, то возвращается индекс текущего числа и дополнения
                return [num_to_index[complement], i]
            # Если не находится, сохраните текущее число и его индекс в словаре
            num_to_index[num] = i

        # Этот подход имеет временную сложность O(n), так как включает один проход по списку,
        # а каждая операция со словарем (вставка и поиск) в среднем занимает O(1).


nums = [2, 7, 11, 15]
target = 9
sol = Solution()
res = sol.twoSum(nums, target)
print(res)
assert res == [0, 1]
