# n, m = map(int, input().split())
# data = list(map(int, input().split()))

# array = [0] * 11

# for x in data:
#     array[x] += 1
    
# result = 0

# for i in range(1, m + 1):
#     n -= array[i]
#     result += array[i]
    
# print(result)

from itertools import combinations

n,m = map(int,input().split())
k = list(map(int,input().split()))

com = list(combinations(k,2))
print(com)
result = len(com)

for i in com:
    if i[0]==i[1]:
        result -= 1
print(result)