import sys
input = sys.stdin.readline 

N= int(input())

answer = []
for _ in range(N):
    method = input().split()
    if method[0] == 'push':
        answer.append(method[1])
    elif method[0] == 'pop':
        if answer:
            print(answer.pop())
        else:
            print(-1)
    elif method[0] == 'size':
        print(len(answer))
    elif method[0] == 'empty':
        if  answer:
            print(0)
        else:
            print(1)
    elif method[0] == 'top':
        if answer:
            print(answer[-1])
        else:
            print(-1)