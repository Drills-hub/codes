N=int(input())

result=1
count=0

for i in range(1,N+1):
    result*=i

result=list(str(result))[::-1]

for j in result:
    if j=="0":
        count+=1
    else:
        break
print(count)