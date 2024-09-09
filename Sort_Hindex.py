'''
어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고
나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 
이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

방법 : 정렬 후 count 
'''
def solution(citations):
    h_index = 0
    citations = sorted(citations, reverse=True)
    print(citations)
    for cite in citations:
        if cite > h_index:
            h_index += 1
        else : break
    
    return h_index

citations = [3, 0, 6, 1, 5] # 3
print(solution(citations))

