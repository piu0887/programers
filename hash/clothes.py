def solution (clothes):

    hash_map ={} # dict() 도 가능
    for item, category in clothes: #이중 배열이니까 [0] - itme [1] - category
        hash_map[category]=hash_map.get(category,0) + 1 
        # clothes 함수를 돌면서 + 1 씩 증가, 없으면 0으로 저장
        # hash.get() 함수 

    answer = 1 # 곱셈 초기값 1
    for category in hash_map:
        answer *= (hash_map[category] + 1) # 입지 않는 경우도 포함 + 1

    return answer -1 # 아무것도 입지 않은경우 빼주기 -1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))

