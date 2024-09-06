'''
자연수 n -> 삼진법 상에서 앞뒤로 뒤집고, 다시 10진법으로 표현
'''
def solution(n):
    answer = 0
    
    re3 = ""
    # 삼진법 만들기
    while n > 0:
        remain = n % 3
        n = n // 3
        re3 = str(remain) + re3
    
    # print(re3)

    # 뒤집기
    # print(re3)
    # re3 = re3[::-1]
    # print(re3)
    # print(re3)

    # 10진법으로 만들기 
    for i in range(len(re3)):
        # print(int(re3[i]))
        answer += (int(re3[i])*3**i)
    return answer

print(solution(45))