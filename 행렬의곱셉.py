'''
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.
'''
def solution(arr1, arr2):
    answer = []
    for row in range(len(arr1)): 
        temp = []
        
        for m2_col in range(len(arr2[0])):
            sum = 0
            for m2_row in range(len(arr2)):
                sum += arr1[row][m2_row] * arr2[m2_row][m2_col]
            temp.append(sum)
        answer.append(temp)
    return answer

arr1=[[1, 4], [3, 2], [4, 1]]	
arr2=[[3, 3], [3, 3]]	
print(solution(arr1, arr2))


# 다른 사람 답
# def productMatrix(A, B):
#     return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]