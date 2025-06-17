from collections import deque

n = int(input())
queue = deque(map(int, input().split()))
stack = []
current = 1  
while queue or stack:
    if queue and queue[0] == current:
        queue.popleft()
        current += 1
    
    elif stack and stack[-1] == current:
        stack.pop()
        current += 1

    elif queue:
        stack.append(queue.popleft())

    else:
        break

if current > n:
    print("Nice")
else:
    print("Sad")