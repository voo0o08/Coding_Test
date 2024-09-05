# 미완
'''
기능마다 개발 속도가 달리 뒤의 기능이 먼저 개발되는 경우 있음 -> 배포 불가능
progresses : 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열
speeds : 각 작업의 개발 속도가 적힌 정수 배열
각 배포마다 몇 개의 기능이 배포되는지를 return
'''
def solution(progresses, speeds):
    days = [] # 각 부분들이 배포에 며칠이 소요되는지 
    for i in range(len(progresses)):
        day = (100-progresses[i]) // speeds[i]
        if (100-progresses[i]) % speeds[i] == 0:
            days.append(day)
        else:
            days.append(day+1)

    for i in rag
    answer = []
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
solution(progresses, speeds)