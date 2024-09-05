def solution(nums):
    max_num = len(nums) // 2 # 종류가 다 다르다는 가정에서 최대 개수
    uni_num = len(set(nums)) # unique한 값
    if max_num > uni_num:
        # 고유값 개수가 최대로 가질 수 있는 개수보다 작다면 return
        return uni_num
    else:
        return max_num
    
nums = [3,1,2,3]
print(solution(nums))