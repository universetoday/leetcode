"""
Given an array of integers arr,
return true if the number of occurrences of each value in the array is unique or false otherwise.
------------------------
Учитывая массив целых чисел arr,
верните true, если количество вхождений каждого значения в массиве уникально, или false в противном случае.
------------------------
EASY
"""
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrence_dict = {}
        for num in arr:
            if num in occurrence_dict:
                occurrence_dict[num] += 1
            else:
                occurrence_dict[num] = 1

        occurrences = list(occurrence_dict.values())
        if len(occurrences) == len(set(occurrences)):
            return True
        else:
            return False


"""
Задача заключается в том, чтобы определить, являются ли количества вхождений каждого элемента в массиве уникальными.
Алгоритм решения:

    Подсчитать количество вхождений каждого элемента массива с помощью словаря (dict).
    Извлечь все значения (т.е. количества вхождений) из словаря и сохранить их в списке.
    Проверить, уникальны ли эти значения. Если все значения уникальны, вернуть true, иначе false.

Пояснение:

    В первой части кода мы создаем словарь occurrence_dict, где ключом является элемент массива, 
    а значением — количество его вхождений.
    Затем мы извлекаем все значения из словаря и сохраняем их в списке occurrences.
    Сравниваем длину списка occurrences с длиной множества, созданного из этого списка. 
    Множество автоматически удаляет дубликаты, поэтому если длины совпадают, 
    это означает, что все количества уникальны.

Таким образом, функция проверяет, уникальны ли количества вхождений элементов в массиве, 
и возвращает true или false в зависимости от результата.    
"""

arr = [1,2,2,1,1,3]
sol = Solution()
res = sol.uniqueOccurrences(arr)
print(res)
assert res == True

arr = [1,2]
sol = Solution()
res = sol.uniqueOccurrences(arr)
print(res)
assert res == False

arr = [-3,0,1,-3,1,1,1,-3,10,0]
sol = Solution()
res = sol.uniqueOccurrences(arr)
print(res)
assert res == True
