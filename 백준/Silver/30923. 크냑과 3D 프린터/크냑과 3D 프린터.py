import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))

surface = []
overlapping = []

for i in range(N):
    h_surface = H[i] * 4 + 2
    surface.append(h_surface)

for j in range(N - 1):
    h_overlapping = min(H[j + 1], H[j]) * 2
    overlapping.append(h_overlapping)

print(sum(surface) - sum(overlapping))