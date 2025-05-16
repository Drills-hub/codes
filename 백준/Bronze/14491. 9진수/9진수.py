t = int(input())
answer=[]
while t>0:
    x=t%9
    t=t//9
    answer.append(x)
answer.reverse()

print("".join(map(str,answer)))