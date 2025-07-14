a,b=map(int,input().split())
c1,c2=map(int,input().split())
n=int(input())

def solution(a,b,n):
    answer=a*n+b
    return answer
f=solution(a,b,n)

if n*c1<=f<=n*c2:
    print(1)
else:
    print(0)    