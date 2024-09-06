'''
피로도 시스템 = 0 이상의 정수 
- 최소 필요 피로도 : 탐험을 시작하기 위해 필요
- 소모 피로도 : 던전 탐험을 마쳤을 때 소모

던전을 최대한 많이 탐험하고 싶음
k = 현재 피로도 
dungeons = [[최소 필요 피로도, 소모 피로도],
            []...]
최대 던전 수 return 
'''
k = 80
dungeons = [[80,20],[50,40],[30,10]]	

def solution(k, dungeons):
    answer = 0
    # sum으로 index list를 생성하자,,,
    dungeons = sorted(dungeons, key=lambda x:x[0])
    for input, output in dungeons:
        sum = input+output
        if k - sum < 0:
            break
        else:
            answer +=1
            k -= sum
        print("k => ",k)
    return answer

print(solution(k, dungeons))