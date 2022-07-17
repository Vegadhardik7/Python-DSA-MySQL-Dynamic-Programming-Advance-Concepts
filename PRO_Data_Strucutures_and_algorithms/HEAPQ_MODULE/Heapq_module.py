import heapq as heap
# This uses minimum value as the Root Node

L= []
heap.heappush(L,20)
heap.heappush(L,14)
heap.heappush(L,5)
heap.heappush(L,15)
heap.heappush(L,10)
heap.heappush(L,2)

print(L)
print(heap.heappop(L))
print(L)

print(heap.heappushpop(L,18))  # deleted min value from the list remove it and added 18
print(L)

L1 = heap.nlargest(3,L)   # Top 3 largest number
print(L1)

L2 = heap.nsmallest(3,L)  # Top 3 smallest number
print(L2)

L3 = [20,14,2,15,10,21]
print("before heapify:",L3)
heap.heapify(L3)   # Make list L3 as heap
print("after heapify:",L3)