import sys
input = sys.stdin.readline

n=int(input())

result=[]
for i in range(n):
    word=input().strip()
    result.append(word)

result = list(set(result))
result.sort(key=lambda x: (len(x), x))

for i in result:
    sys.stdout.write(i+"\n")