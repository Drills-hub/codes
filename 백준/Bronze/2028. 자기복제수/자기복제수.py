def solution(num:int):
    len_n=len(str(num))
    result=(num**2)%10**len_n
    if num==result:
        return "YES"
    return "NO"

n = int(input())
for _ in range(n):
    num=int(input())
    print(solution(num))