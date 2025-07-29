import sys
input=sys.stdin.readline

N=int(input())
atm_time=list(map(int,input().split()))
atm_time.sort()

answer=[atm_time[0]]
for i in range(1,N):
    pre_answer=answer[-1]
    answer.append(pre_answer+atm_time[i])
print(sum(answer))