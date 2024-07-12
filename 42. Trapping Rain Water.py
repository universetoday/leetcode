"""
Given n non-negative integers representing an elevation map
where the width of each bar is 1,
compute how much water it can trap after raining.
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Для решения этой задачи можно использовать два указателя
        для эффективного вычисления объекма удериваемой воды.
        """
        # 1. Если height пуст, то сразу вернуть 0
        if not height:
            return 0
        # 2. Инициализация двух указателей left и right, указывающих на начало и конец массива
        left = 0
        right = len(height) - 1
        # 3. Инициализация left_max и right_max для хранения максимальных высот слева и права от
        # текущих указателей, а также water_trapped для хранения общего объема удерживаемой воды
        left_max = height[left]
        right_max = height[right]
        water_trapped = 0
        # 4. Пока left меньше right, выполняем следующие действия
        while left < right:
            # Если left_max меньше right_max, то сдвигаем left вправо
            # Обновляем left_max
            # Добавляем разницу между left_max и текущей высотой к water_trapped
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water_trapped += left_max - height[left]
            # Иначе
            # Сдвигаем курсор right влево
            # Обновляем right_max
            # Добавляем разницу между right_max и текущей высотой к water_trapped
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water_trapped += right_max - height[right]
        return water_trapped


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
sol = Solution()
res = sol.trap(height)
print(res)
assert res == 6

height = [4, 2, 0, 3, 2, 5]
sol = Solution()
res = sol.trap(height)
print(res)
assert res == 9
