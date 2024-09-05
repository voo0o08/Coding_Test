'''
배열 arr의 각 원소는 숫자 0~9로 구성
배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 제거하고 싶음
단, 제거된 후 수를 반환할 때 arr 원소들의 순서 유지 
'''
def solution(arr):
    answer = []
    pre = arr[0]
    for i in range(len(arr)-1):
        if pre != arr[i+1]:
            answer.append(pre)
        pre = arr[i+1]
    answer.append(pre)
    
    return answer

arr = [1,1,3,3,0,1,1]
print(solution(arr))