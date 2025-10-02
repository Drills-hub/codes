import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    count = 0
    child = list(map(int, input().split()))
    idx = child[0]
    child = child[1:]

    line = []

    for i in range(len(child)):
        current = child[i]
        position = 0
        for j in range(len(line)):
            if line[j] > current:
                position = j
                break
            position = j + 1
        steps_back = len(line) - position
        count += steps_back
        line.insert(position, current)

    print(idx, count)