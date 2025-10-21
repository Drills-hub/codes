def solution(num: int) :
    a=num//3
    b=num//7
    c=num//21
    answer = (3*a*(a+1)//2) + (7*b*(b+1)//2) - (21*c*(c+1)//2)
    return answer
    
n = int(input())
num_list = list(map(int, input().split()))

for num in num_list:
    print(solution(num))