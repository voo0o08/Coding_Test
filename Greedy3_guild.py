'''
모험가 길드
- 모험가 N명의 공포도 층정
- 공포도가 X인 모험가는 반드시 X명 이상으로 구성해야 함
- 최대 몇 개의 모험가 그룹을 만들 수 있을까
- N이 주어졌을 때 여행을 떠날 수 있는 그룹의 수의 최댓값
- 모든 모험가가 떠날 필요는 없음 

생각 : 공포도가 낮은 애들끼리 빨리 보내자
'''
n = int(input("모험가의 수 N을 입력하시오 : "))
# 공포도 
x = list(map(int, input("모험가의 공포도를 입력하시오 : ").split()))

x.sort()
cnt = 0
temp = []
for i in range(len(x)):
    point = x[i] 
    temp.append(point)
    if point == len(temp):
        temp = []
        cnt += 1
print(cnt)