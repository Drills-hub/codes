import heapq

gift_queue = []

def solution(gift: list):
    if gift[0] == "0":
        if gift_queue:
            return -heapq.heappop(gift_queue)
        else:
            return -1
    else:
        for g in gift[1:]:
            heapq.heappush(gift_queue, -int(g))
        return None

n = int(input())
for _ in range(n):
    gift = input().split()
    result = solution(gift)
    if result is not None:
        print(result)