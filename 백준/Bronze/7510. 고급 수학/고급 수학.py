import sys
input = sys.stdin.readline

n = int(input())
for i in range(1,n+1):
    s = list(map(int,input().split()))
    s.sort(reverse=True)
    if s[0]**2 == s[1]**2 + s[2]**2:
        print(f"Scenario #{i}:\nyes\n")
    else:
        print(f"Scenario #{i}:\nno\n")