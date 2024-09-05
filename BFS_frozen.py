'''
음료 얼먹
N X M 크기의 얼음 틀
구멍이 뚫린 부분은 0
칸막이가 존재하는 부분은 1
구멍이 뚫린 부분이 상하좌우 붙으면 연결되어 있는 것
얼음틀이 주어 졌을 때 생성
'''
n, m = map(int, input("세로 N, 가로 M : ").split())
print(n, m)
graph = [[0,0,1,1,0],
        [0,0,0,1,1],
        [1,1,1,1,1],
        [0,0,0,0,0]]

# DFS로 특정 노드를 방문하고 연결된 모든 노드를 방문하는 함수 정의
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        # dfs(x - 1, y)
        # dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False



# 모든 노드(위치)에 대해 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1


print(result)
