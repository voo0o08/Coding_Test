'''
1명 배고 모두 완주
participant : 마라톤에 참여한 선수들 명단
completion : 완주한 사람들 명단
완주 못한 선수의 이름을 return
'''
# 단순 정렬 -> 비교 -> 다르면 출력
# 문제 : 데이터가 많아지면 시간 복잡도 증가
def solution(participant, completion):
    for win in completion:
        participant.remove(win)
    print(participant)
    
    return participant[0]

participant = ["leo", "kiki", "eden"]	
completion = ["eden", "kiki"]	
solution(participant, completion)