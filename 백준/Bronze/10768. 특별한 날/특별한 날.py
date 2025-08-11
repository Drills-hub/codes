import sys
input = sys.stdin.readline

N=int(input())
M=int(input())

if N==2:
    if M < 18:
        print("Before")
    elif M==18:
        print("Special")
    else:
        print("After")
elif N < 2:
    print("Before")
else:
    print("After")