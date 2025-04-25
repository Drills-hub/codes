n=input()
result=[]

for i in n:
    result.append(int(i))
result.sort(reverse=True)

print(''.join(map(str,result)))

