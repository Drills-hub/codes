import sys
input = sys.stdin.readline

n = int(input())

answer = []
for i in range(1,n+1):
    x,y=map(int,input().split())
    ppi=((x**2+y**2)**(1/2))/77
    answer.append((ppi,i))

answer.sort(key=lambda x: (-x[0], x[1])) 

for i in answer:
    print(i[1])