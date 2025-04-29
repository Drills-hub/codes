import sys
input = sys.stdin.readline

N= int(input())

count = 0
for i in range(1, int(N**0.5)+1):
    if N % i == 0:
        count += 1
        if i != N//i:
            count += 1
        
print(count)