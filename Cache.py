'''
지도에서 도시 이름을 검색하면 해당 도시와 관련된 맛집 게시물들을 데이터베이스에서 읽어 보여주는 서비스를 개발 중
DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성

# cacheSize가 0인 경우를 고려해줘야 함!!
'''
def solution(cacheSize, cities):
    hit = 1
    miss = 5
    if cacheSize == 0:
        return len(cities) * miss
    cities = map(str.upper, cities)
    answer = 0
    cache = []
    
    for city in cities:
        # cache안에 있다면
        print(f"================= {city}")
        print(f"전 => {cache}")
        if city not in cache:
            answer += miss
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache = cache[1:]
                cache.append(city)
        else: 
            # hit하면 제일 뒤로 빠져야함 
            temp = []
            for i in cache:
                if i != city:
                    temp.append(i)
            temp.append(city)
            cache = temp

            # hit초 추가 
            answer += hit 
        print(f"후 => {cache}")
    return answer


ccitiesacheSize = 0
cities = ["LA", "LA"] # 21
print(solution(ccitiesacheSize, cities)) 