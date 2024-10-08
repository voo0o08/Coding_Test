# 계산 결과 memoization 리스트 초기화
d = [0] * 100

# fibo 함수를 재귀, 다이나믹 프로그래밍을 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x-1) + fibo(x-2)
    
    return d[x]

print(fibo(99))