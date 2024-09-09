'''
1. n행 n열 크기의 비어있는 2차원
2. i = 123n에 대해 1행 1열~i행i열 영역내의 모든 빈 칸의 숫자를 i로 채움
3. 1행+2행.... -> 새로운 1차원 배열 arr

-> n*n번 for문을 도는 것이 좀 버거운 듯 하다...
'''

def solution(n, left, right):
    # 1. n행 n열 크기의 비어있는 2차원
    n_arr = [[max(i, j) + 1 for j in range(n)] for i in range(n)]
    # print(n_arr)

    # 2.1행 1열~i행i열 영역내의 모든 빈 칸의 숫자를 i로 채움
    # for i in range(n):
    #     n_arr[i][i] = i+1
    #     for j in range(i, n):
    #         n_arr[i][j] = j+1
    #         n_arr[j][i] = j+1
    # print(n_arr)
    
    
    # 새로운 1차원 배열 arr
    arr = []
    for l in n_arr:
        arr += l
    return arr[left:right+1]