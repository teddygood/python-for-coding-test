import heapq

n = int(input())

heap = []
result = 0

for i in range(n):
    heapq.heappush(heap, int(input()))

while len(heap) != 1:
    result += heapq.heappop(heap) + heapq.heappop(heap)
    heapq.heappush(heap, result)
    
print(result)