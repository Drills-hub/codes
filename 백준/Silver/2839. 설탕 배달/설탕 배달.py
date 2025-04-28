import sys
input=sys.stdin.readline

N = int(input())

answer=[]

if N%3==0:
    m=N//3
    answer.append(m)
if N%5==0:
    m=N//5
    answer.append(m)

for x in range(N//3+1):
    for y in range(N//5+1):
        if 3*x+5*y==N:
            answer.append(x+y)

if answer:
    print(min(answer))
else:
    print(-1)
    
    