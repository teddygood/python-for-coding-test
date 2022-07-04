n = int(input())
fear_list = list(map(int, input().split()))
fear_list.sort()

group_count = 0

p = 0 # 모험가 수

for i in fear_list:
    p += 1
    if p >= i:
        group_count += 1
        p = 0

print(group_count)