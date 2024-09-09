'''
- 코니는 각 종류별로 최대 1가지 의상만 착용
- 착용한 의상의 일부가 겹쳐도 완전히 똑같지 않다면 OK
- 하루에 최소 한 개의 의상을 입음 

=> clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성

방법 : Dictionary 사용
'''
def solution(clothes):
    answer = 1
    clothes_dict = {}
    for name, key in clothes:
        if key in clothes_dict.keys():
            clothes_dict[key].append(name)
        else:
            clothes_dict[key] = [name]
    
    for key, val in clothes_dict.items():
        print("============", len(val)+1)
        answer *= (len(val)+1)
    print(clothes_dict)
    answer -= 1 # 모두 착용 안할 확률 없애기
    return answer

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]] # 5
print((solution(clothes)))