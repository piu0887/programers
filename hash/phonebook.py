def solution (phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1 
        # phone_book에 있는 phone_number를 찾아서 hash_map[phone_number]에 value를 1준다
    
    for phone_number in phone_book:
        # phone_book에 있는 배열을 하나씩 
        startwith = ""
        # 문자열 선언
        for number in phone_number:
            # phone_number에 있는 문자열 하나씩
            startwith += number

            if startwith in hash_map and startwith != phone_number:
                return False
        
    return True

print(solution(["6", "12" , "6789"]))