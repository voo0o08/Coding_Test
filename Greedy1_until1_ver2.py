'''
N이 1이 될 때까지 두 과정 중 하나를 반복 수행
1. N에서 1을 뺌 
2. N을 K로 나눔 
단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택 가능
N이 1이 될 때까지 과정을 수행하는 최소 횟수
-> 일단 나누는 게 훅훅 떨어지니까,,,
'''
# 25, 5
N, K = map(int, input("N K를 입력하시오 : ").split())

cnt = 0
# 이전 과정과 달리 한번에 해결

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (N//K)*K # 가장 가까운 K로 나누어 떨어지는 수
    cnt += (N-target)

    # 정지조건 : N이 K보다 작을 때(더 이상 나눌 수 없을 때)
    if N<K:
        break

    N //= K
    cnt += 1

print(cnt) 