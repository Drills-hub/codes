import sys
input = sys.stdin.readline

A,B = map(int,input().split())

answer = []
for i in range(1,B+1):
    for j in range(i):
        answer.append(i)        
print(sum(answer[A-1:B]))