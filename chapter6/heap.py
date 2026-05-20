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
            self.maxHeapify(A, 0, len(A))
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


    def maxHeapify(self, A: List[Any], i: int, size: int):
        """
        Build a max-heap
        """
        while True:
            greatest = i
            left = 2*i + 1
            right = 2*i + 2
            if left < size and A[left] > A[greatest]:
                greatest = left
            if right < size and A[right] > A[greatest]:
                greatest = right
            if greatest == i: break
            A[greatest], A[i] = A[i], A[greatest]
            i = greatest

    
    def buildMinHeap(self, A: List[Any]):
        for i in range(len(A)//2-1, -1, -1):
            self.minHeapify(A, i)

    
    def buildMaxHeap(self, A: List[Any]):
        for i in range(len(A)//2-1, -1, -1):
            self.maxHeapify(A, i, len(A))


    def heapsort(self, A: List[Any]):
        """ Sorts a max-heap """
        self.buildMaxHeap(A)
        print(A)
        n = len(A)
        while n > 1:
            A[n-1], A[0] = A[0], A[n-1]
            n -= 1
            self.maxHeapify(A, 0, n) 


if __name__ == "__main__":
    A = [
        (5, 'write code'), 
        (7, 'release product'),
        (1, 'write spec'), 
        (3, 'create tests')
    ]
    Heap().heapsort(A)
    print(A)