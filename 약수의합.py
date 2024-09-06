'''
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
'''
n = int(input("정수 n을 입력하시오 : "))
n_list = []

def solution(n):
    for i in range(1, n+1):
        if n % i == 0:
            n_list.append(i)

    return sum(n_list)

# sum([i for i in range(1, n+1) if n%i == 0]) -> 리스트 컴프리헨션 써도 됨 



print()
print(solution(n))