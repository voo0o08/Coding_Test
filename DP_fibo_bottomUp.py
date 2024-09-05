# 계산 결과 memoization 리스트 초기화
d = [0] * 100

# 시작 부터 채우고 출발
d[0] = 1
d[1] = 1

n = 99
for i in range(2, n):
    d[i] = d[i-1] + d[i-2]
print(d[n-1])