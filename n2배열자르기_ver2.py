'''
1. n행 n열 크기의 비어있는 2차원
2. i = 123n에 대해 1행 1열~i행i열 영역내의 모든 빈 칸의 숫자를 i로 채움
3. 1행+2행.... -> 새로운 1차원 배열 arr

이 순서를 따르면,,,
예제까지는 괜찮지만 test case 일부 run time error가 난다
한큐에 해결할 방법이 필요해,,,
'''

def solution(n, left, right):
    n_arr = []
    for i in range(left, right+1):
        a = i // n# 몫 
        b = i % n# 나머지
        max_val = max(a,b)
        n_arr.append(max_val + 1)
    return n_arr

print(solution(4, 7, 14))