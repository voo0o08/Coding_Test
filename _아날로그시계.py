'''
시침, 분침, 초침은 각각 다르게 일정하게 움직임 
시계의 기능 : 초침이 시침/분침이 겹칠 떄 알람
-> 특정 시간 동안 알람이 울린 횟수는?

방법 : ?
'''
from datetime import timedelta

def count_alarms(h1, m1, s1, h2, m2, s2):
    # 시간 계산을 위해 timedelta 사용
    start_time = timedelta(hours=h1, minutes=m1, seconds=s1)
    end_time = timedelta(hours=h2, minutes=m2, seconds=s2)
    
    # 종료 시간이 시작 시간보다 이르면 하루 더해줌
    if end_time < start_time:
        end_time += timedelta(days=1)
    
    # 두 시간 사이의 전체 초 계산
    total_seconds = (end_time - start_time).total_seconds()
    
    # 초침과 분침이 겹치는 순간: 60초마다
    minute_overlap = total_seconds // 60
    
    # 초침과 시침이 겹치는 순간: 약 3927.27초마다 (하루에 22번)
    hour_overlap = total_seconds // 3927.27
    
    # 초침, 분침, 시침이 동시에 겹치는 순간: 43200초마다 한 번 (12시간에 한 번)
    all_overlap = total_seconds // 43200
    
    # 초침과 분침, 시침이 겹치는 순간에서 세 바늘이 동시에 겹치는 순간을 중복 제거
    total_alarms = int(minute_overlap + hour_overlap - all_overlap)
    
    return total_alarms

# 예시 입력
h1, m1, s1 = 0, 5, 30
h2, m2, s2 = 0, 7, 0
result = count_alarms(h1, m1, s1, h2, m2, s2)
print(result)