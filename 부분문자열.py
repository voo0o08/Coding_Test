'''
크기가 작은 부분 문자열 
숫자로 이루어진 문자열 t, p
t가 p보다 작은 부분의 횟수를 count 
'''
t = "500220839878"
p = "7"

def solution(t, p):
    answer = 0
    length = len(p)
    num2 = int(p)
    for i in range(len(t) - length + 1):
        num1 = int(t[i:i+length])
        if num1 <= num2:
            answer += 1
        print(num1, "   ", num2)
    return answer

solution(t, p)
