def typo(N):
    for _ in range(N):
        a,b=input().split()
        a=int(a)
        print(b[:a-1] + b[a:])

typo(int(input()))