'''
자연수 n을 연속한 자연수들로 표현하는 방법이 여러개
n을 주면 몇가지 방법으로 표현할 수 있는지 

방법 : 
- 같으면 합격
- 작으면 넘어가고
- 초과하면 탈락
'''
def solution(n):
    answer = 0
    sum = 0
    for i in range(1, n+1):
        recent = i
        # print(f"=========== {i} ==========")
        while sum <= n:
            if sum == n:
                answer += 1 # 횟수 증가 

            sum += recent
            recent += 1
            # print(sum)
        sum = 0 # sum 초기화 
    return answer

print(solution(15))