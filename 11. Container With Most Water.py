"""
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.
Notice that you may not slant the container.
--------------------
Задача: дан целочисленный массив height длины n.
Есть n вертикальных линий, таких что два конца i-й линии находятся в точках (i, 0) и (i, height[i]).

Найдите две линии, которые вместе с осью x образуют контейнер,
такой что контейнер содержит максимальное количество воды.

Верните максимальное количество воды, которое может хранить контейнер.
--------------------
MEDIUM
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Используем два указателя  left и right
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            # Вычисляем ширину контейнера между указателями
            width = right - left
            # Вычисляем высоту контейнера
            current_height = min(height[left], height[right])
            current_water = width * current_height
            max_water = max(current_water, max_water)

            # Сдвигаем указатель left вправо, если высота слева меньше высоты справа
            if height[left] < height[right]:
                left += 1
            # Иначе указатель right вправо
            else:
                right -= 1
        return max_water


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
sol = Solution()
res = sol.maxArea(height)
print(res)
assert res == 49

height = [1, 1]
sol = Solution()
res = sol.maxArea(height)
print(res)
assert res == 1

