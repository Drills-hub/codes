n, k = map(int, input().split())
queue = list(range(1, n + 1))
result = []
idx = 0

while queue:
    idx = (idx + k - 1) % len(queue)
    result.append(queue.pop(idx))

print("<" + ", ".join(map(str, result)) + ">")