'''
음료 얼먹
N X M 크기의 얼음 틀
구멍이 뚫린 부분은 0
칸막이가 존재하는 부분은 1
구멍이 뚫린 부분이 상하좌우 붙으면 연결되어 있는 것
얼음틀이 주어 졌을 때 생성
'''
N, M = input("세로 N, 가로 M")
mold = [[0,0,1,1,0],
        [0,0,0,1,1],
        [1,1,1,1,1],
        [0,0,0,0,0]]
print(list(map(int, input())))

# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))


cnt = 0
for i in range(N):
    for j in range(M):
        if mold[N, M]==0:
            if mold[N-1, M]