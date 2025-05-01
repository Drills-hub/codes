N=int(input())

for _ in range(N):
    a,b=input().split()
    a=int(a)
    result = b[:a-1] + b[a:]
    print(result)