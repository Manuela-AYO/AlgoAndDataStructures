"""
This file is an implementation of the heap operations.
Heaps are array that can be seen as fully complete binary trees. 
We have 2 kinds of heaps: min-heap and max-heap.
The min-heap respects the min-heap property which states for 
any node other than the parent, A[parent(i)] <= A[i]. The 
sign is reversed for the max-heap(>=)
"""
from typing import List, Any

class Heap:
    @staticmethod
    def parent(i: int): return (i-1) // 2


    def heappop(self, A: List[Any]):
        try:
            A[-1], A[0] = A[0], A[-1]
            item = A.pop()
            self.minHeapify(A, 0)
            return item
        except IndexError:
            raise IndexError("The heap is empty")
        
    
    def heappop_max(self, A: List[Any]):
        try:
            A[-1], A[0] = A[0], A[-1]
            item = A.pop()
            self.maxHeapify(A, 0)
            return item
        except IndexError:
            raise IndexError("The heap is empty")


    def heappush(self, A: List[Any], item: Any):
        i = len(A)
        A.append(item)
        while i > 0 and A[self.parent(i)] > A[i]:
            A[self.parent(i)], A[i] = A[i], A[self.parent(i)]
            i = self.parent(i)

    
    def heappush_max(self, A: List[Any], item: Any):
        i = len(A)
        A.append(item)
        while i > 0 and A[self.parent(i)] < A[i]:
            A[self.parent(i)], A[i] = A[i], A[self.parent(i)]
            i = self.parent(i)


    def minHeapify(self, A: List[Any], i: int):
        """
        Build a min-heap
        """
        while True:
            smallest = i
            left = 2*i + 1
            right = 2*i + 2
            if left < len(A) and A[left] < A[smallest]:
                smallest = left
            if right < len(A) and A[right] < A[smallest]:
                smallest = right
            if smallest == i: break
            A[smallest], A[i] = A[i], A[smallest]
            i = smallest


    def maxHeapify(self, A: List[Any], i: int):
        """
        Build a max-heap
        """
        while True:
            greatest = i
            left = 2*i + 1
            right = 2*i + 2
            if left < len(A) and A[left] > A[greatest]:
                greatest = left
            if right < len(A) and A[right] > A[greatest]:
                greatest = right
            if greatest == i: break
            A[greatest], A[i] = A[i], A[greatest]
            i = greatest


if __name__ == "__main__":
    my_heap = Heap()
    h = []
    my_heap.heappush_max(h, (5, 'write code'))
    my_heap.heappush_max(h, (7, 'release product'))
    my_heap.heappush_max(h, (1, 'write spec'))
    my_heap.heappush_max(h, (3, 'create tests'))
    #value = my_heap.heappop(h)
    #print(value)
    print(h)