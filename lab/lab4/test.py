import random
from DHeap import DHeap
a=[0]+[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
heap=DHeap(3,a)

heap.Heapifyall()
print(heap.HeapArray)
heap.ExtractMax()
print(heap.HeapArray)
#重置数组
heap.HeapArray=[0]+[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
heap.size+=1
heap.Heapifyall()
heap.IncreaseKey(10,28)

print(heap.HeapArray)