"""
Design a class to find the kth largest element in a stream.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

    KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
    int add(int val) Appends the integer val to the stream and returns the element
    representing the kth largest element in the stream.

------------------------

------------------------
EASY
"""
import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)

        return self.min_heap[0]


"""
Задача состоит в том, чтобы разработать класс, 
который будет находить k-тый по величине элемент в потоке чисел. 
Этот элемент будет не уникальным, а просто k-тым по порядку в отсортированном списке.

Объяснение:

    Инициализация (__init__ метод):
        В методе __init__ мы создаем мин-кучу (min_heap), 
        которая будет хранить только k самых больших элементов из потока чисел.
        Инициализация происходит путем добавления чисел из nums с помощью метода add.

    Добавление нового числа (add метод):
        Если текущий размер кучи меньше k, мы просто добавляем новый элемент.
        Если число больше минимального элемента в куче, мы заменяем минимальный элемент на новый. 
        Это гарантирует, что в куче всегда хранятся k самых больших элементов.
        Возвращается минимальный элемент из кучи, который и является k-тым по величине элементом.
        
В этом примере, min_heap будет выглядеть следующим образом на каждом этапе:

    После kthLargest.add(3): [4, 5, 8]
    После kthLargest.add(5): [5, 5, 8]
    После kthLargest.add(10): [5, 8, 10]
    После kthLargest.add(9): [8, 9, 10]
    После kthLargest.add(4): [8, 9, 10]
"""

kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))   # вернет 4
print(kthLargest.add(5))   # вернет 5
print(kthLargest.add(10))  # вернет 5
print(kthLargest.add(9))   # вернет 8
print(kthLargest.add(4))   # вернет 8


