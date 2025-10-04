import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cats = list(map(int, input().split()))

cats.sort()

left = 0
right = n - 1
max_people = 0

while left < right:
    if cats[left] + cats[right] <= k:
        max_people += 1
        left += 1
        right -= 1
    else:
        right -= 1

print(max_people)