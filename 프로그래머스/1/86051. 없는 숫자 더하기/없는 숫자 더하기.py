def solution(numbers):
    regular_num= [0,1,2,3,4,5,6,7,8,9]
    answer = set(regular_num)-set(numbers)
    return sum(answer)