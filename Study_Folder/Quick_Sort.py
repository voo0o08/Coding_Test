# 퀵 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    # 정지 조건 : 데이터의 크기가 1개인 경우
    if start >= end:
        return

    pivot_idx = start
    left_idx = start+1
    right_idx = end

    while (left_idx <= right_idx):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left_idx <= end and array[left_idx] <= array[pivot_idx]):
            left_idx+=1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right_idx > start and array[right_idx] >= array[pivot_idx]):
            right_idx -= 1
        
        # 엇갈리는 부분 
        if left_idx > right_idx:
            array[right_idx], array[pivot_idx] = array[pivot_idx], array[right_idx]
        # 엇갈리지 않으면 작은 데이터와 큰 데이터 교체 
        else: 
            array[left_idx], array[right_idx] = array[right_idx], array[left_idx]

    # 분할 정복
    quick_sort(array, start, right_idx-1) # pivot 왼쪽
    quick_sort(array, right_idx+1, end) # pivot 오른쪽 

quick_sort(array, 0, len(array) - 1) # array, start_idx, end_idx
print(array)