'''
시침, 분침, 초침은 각각 다르게 일정하게 움직임 
시계의 기능 : 초침이 시침/분침이 겹칠 떄 알람
-> 특정 시간 동안 알람이 울린 횟수는?

방법 : ?
'''
def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    # 동시(12시 정각)에 만나면 1회
    h = h2-h1
    m = m2-m1
    s = s2-s1

    # totla time
    total = h*60*60 + m * 60 + s
    
    print(total // 60)
    print(total // 3927.27)
    print(h, m, s)
    return answer

h1, m1, s1,	h2,	m2,	s2 = 12, 0, 0, 12, 0, 30 # ressult = 1
h1, m1, s1,	h2,	m2,	s2 = 0, 5, 30, 0, 7, 0 # ressult = 2
print(solution(h1, m1, s1, h2, m2, s2))