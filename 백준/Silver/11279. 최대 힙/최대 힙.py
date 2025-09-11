import sys
import heapq

input = sys.stdin.readline
N = int(input())

heap = []
answer = []
for i in range(N):
    i = int(input())
    if i == 0:
        if heap:
            answer.append(str(-heapq.heappop(heap)))
        else:
            answer.append("0")
    else:
        heapq.heappush(heap, -i)

sys.stdout.write("\n".join(answer))