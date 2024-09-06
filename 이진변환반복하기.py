'''
0과 1로 이루어진 문자열 x
1. x의 모든 0 제거
2. x의 길이를 c라 하면, x를 "c를 2진법으로 표현한 문자열"로 변환

s가 1이 될때까지 반복 

이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return

return [2진 변환 횟수, 제거된 0의 개수]
'''

def solution(s):
    cnt = 0
    zero_cnt =  0
    # s가 1이 되면 중단
    while int(s) > 1:
        print(s)
        # a 문자열에 0을 제거하고 1만 남기기 
        a = ""
        for i in s:
            if i == "1":
                a += i
            else:
                zero_cnt += 1

        # print("a ==> ", a)
        # c=s의 길이 -> 이진 변환
        c = len(a)

        result = "" # 이진화 결과 
        while c != 0:
            val = c % 2
            c = c // 2
            if val == 0:
                result = "0" + result
            else:
                result = "1" + result
            
   
       
        

        cnt += 1 # 이진화 횟수
        
        s = result
        # print(result)
    

    answer = [cnt, zero_cnt]    
    return answer

s = "110010101001"
print(solution(s))