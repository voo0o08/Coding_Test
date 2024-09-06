'''
S사 각 부서 물품 구매를 위한 금액 조사
전체 예산은 정해짐, 최대한 많은 부서의 물품을 구매해주고 싶음
구매해 줄 때는 각 부서가 신청한 금액 모두 지원
d : 부서별로 신청한 금액 배열
budget : 예산
최대 몇 개의 부서에 물품 조달 가능?

생각 : 
sort 시켜서 금액 적은 부서부터 채우기 
'''
def solution(d, budget):
    answer = 0 # 몇개의 부서
    d.sort() # 정렬
    print(d)

    for i in range(len(d)):
        # print("d => ", d)
        # print("잔액 => ", budget)
        if d[i] <= budget:
            budget -= d[i]
            answer += 1
        else: break
        # print()
    return answer

d = [2,2,3,3]	
budget = 10
print(solution(d, budget))