'''
- Key : 고유 값, Hash의 Input
- Hash Table(Hash Map) : Key-Value 매핑으로 데이터를 저장하는 자료구조
- Hash Function : 임의의 값을 고정된 길이의 데이터로 변환하는 함수
- Hash : 해시 함수의 output으로 해시 값과 매칭되어 버킷에 저장
- Hash Value(Hash Addresss) : 키에 해시 함수를 적용하여 얻은 해시 값 -> 인덱스 느낌?
- Bucket : 한 개의 데이터를 저장할 수 있는 공간
'''
hash_table = [0 for _ in range(100)] # np.zeros 

def hash_function(key):
    # 파이썬 내장함수 hash
    return hash(key) % 100

def set_data(key, value):
    # hash value를 받아옴
    hash_value = hash_function(key)
    hash_table[hash_value] = value # Hash Map의 주소에 value를 넣어줌 

def get_data(key):
    hash_value = hash_function(key)
    return hash_table[hash_value]

set_data("Lee", 2022)
set_data("hello", 77)
print(get_data("Lee"))
print(get_data("hello"))