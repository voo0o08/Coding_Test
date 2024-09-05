'''
곱하기 혹은 더하기
각 자리가 0~9로 이루어진 문자열 S가 주어졌을 때, 
-> 방향으로 하나씩 모든 숫자를 확인하며 숫자 사이에 X 혹은 +를 넣어 가장 큰 수를 구하는 프로그램
연산 우선 순위 무시 무조건 -> 방향

생각 : 0, 1만 더하고 나머지는 다 곱하면 된다!
'''
S = input("숫자 문자열을 입력하시오 : ")

answer = int(S[0])
for i in range(len(S)-1):

    if S[i] < "1" or S[i+1] < "1":
        answer += int(S[i+1])
    else:
        answer *= int(S[i+1])


print(answer)

