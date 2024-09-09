'''
- 코니는 각 종류별로 최대 1가지 의상만 착용
- 착용한 의상의 일부가 겹쳐도 완전히 똑같지 않다면 OK
- 하루에 최소 한 개의 의상을 입음 

=> clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성

방법 : Hash 사용
'''
def solution(clothes):
    clothes_type = {}

    for _, key in clothes:
        if key not in clothes_type:
            clothes_type[key] = 2
        else:
            clothes_type[key] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]] # 5
print((solution(clothes)))