'''
500원 100원 50원 10원이 무한히 존재한다
N원일 때 거슬러 주어야 할 동전의 최소 개수 
-> 큰 돈 부터 시작
- 화폐의 종류가 K라고 할 때, 소스코드의 시간 복잡도는 O(K)
'''
N = 1260
cnt = 0
coins = [500, 100, 50, 10]
for cost in coins:
    cnt += N // cost
    N -= (N // cost) * cost
print(cnt)