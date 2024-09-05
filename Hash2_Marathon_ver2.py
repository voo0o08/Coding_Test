'''
1명 배고 모두 완주
participant : 마라톤에 참여한 선수들 명단
completion : 완주한 사람들 명단
완주 못한 선수의 이름을 return
'''
# Hash로 해결 하기 
# 문제 : 데이터가 많아지면 시간 복잡도 증가
def solution(participant, completion):
    hashDict = {}
    sumHash = 0

    for part in participant:
        hashDict[hash(part)] = part # 해쉬값:참가자
        sumHash += hash(part)

    # completion의 sum(hash) 빼기
    for comp in completion:
        sumHash -= hash(comp)

    # 남은 값 = 완주 못한 선수의 Hash 값
    return hashDict[sumHash]

participant = ["leo", "kiki", "eden"]	
completion = ["eden", "kiki"]	
print(solution(participant, completion))