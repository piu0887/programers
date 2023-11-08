def solution(s):
    
    stack = []

    for char in s :
        if char == '(' :
            stack.append(char)
        else:
            if stack == [] :
                return False
            elif char ==')' :
                stack.pop()
    if stack :
        return False
    return True
        
s =["(())()"]
print(solution(s))
