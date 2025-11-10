import sys
input = sys.stdin.readline

def find_title(power, powers, titles):
    left, right = 0, len(powers) - 1
    result = 0  # 기본값은 가장 낮은 칭어
    
    while left <= right:
        mid = (left + right) // 2
        if power <= powers[mid]:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return titles[result]

n, m = map(int, input().split())
titles = []
powers = []

for _ in range(n):
    title, power = input().split()
    power = int(power)
    titles.append(title)
    powers.append(power)

for _ in range(m):
    power = int(input())
    print(find_title(power, powers, titles))