def solution(s):
    stack = []
    for i in s:
        if len(s) % 2 > 0:
            return False
        
        elif i == '(':
            stack.append(i)
            
        else:
            if not stack: 
                return False
            stack.pop()
    return len(stack) == 0