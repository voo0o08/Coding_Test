array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만 가진다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot] # pivot보다 작은 값은 left 배열 
    right_side = [x for x in tail if x >= pivot] # pivot보다 큰 값은 right 배열

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행 후 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))