'''
두 수 중 큰 수를 작은 수로 나눕니다.
나머지가 0이면 작은 수가 최대 공약수가 됩니다.
나머지가 0이 아니면 작은 수가 큰 수가 되고, 나머지를 작은 수로 대체하고 1단계로 돌아갑니다.
'''
# 재귀함수 
def gcd(num1, num2):
    if num1 % num2 == 0:
        return num2
    else:
        return gcd(num2, num1%num2)        
num1, num2 = 192, 162
print(gcd(num1, num2))