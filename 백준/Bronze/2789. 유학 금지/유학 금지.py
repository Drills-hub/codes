import sys
input = sys.stdin.readline
s= input()
answer=[]
check=["C","A","M","B","R","I","D","G","E"]
for i in s:
    if i not in check:
        answer.append(i)
        
print("".join(answer))