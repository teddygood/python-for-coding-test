# DP 테이블
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

# 반복문으로 구현(bottom-up)
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])