n, k = map(int, input().split())

gameer_list = list(range(1, n+1))
result_list = []
spot = 0

for _ in range(n):
    spot = (spot + k - 1) % len(gameer_list)
    result_list.append(gameer_list.pop(spot))

print(f"<{', '.join(map(str, result_list))}>")