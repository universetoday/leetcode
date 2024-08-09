"""
Given an integer array nums sorted in non-decreasing order,
remove some duplicates in-place such that each unique element appears at most twice.
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.
-----------------
Дан массив чисел, отсортированный в неуменьшающемся порядке, удалите некоторые дубликаты на месте,
так чтобы каждый элемент появлялся максимум дважды. Относительный порядок элементов должен оставаться тем же самым.

Так как невозможно изменить длину массива в некоторых языках, вы должны поместить результат в первую часть массива.
-----------------
MEDIUM
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 2
        # Указатель для позиции следующего уникального элемента
        write_index = 2
        # Проходим по массиву, начиная с третьего элемента
        for i in range(2, len(nums)):
            # Если текущий элемент не равен элементу в позиции write_index - 2, то записываем его
            if nums[i] != nums[write_index - 2]:
                nums[write_index] = nums[i]
                write_index += 1

        return write_index


nums = [1, 1, 1, 2, 2, 3]
k = Solution().removeDuplicates(nums)
print(nums[:k])  # Вывод: [1, 1, 2, 2, 3]
print(k)         # Вывод: 5






