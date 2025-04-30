n=int(input())
num_list=list(map(int,input().split()))

num_list.sort()
G=[]
answer=0
for i in range(len(num_list)):
    if i==0:
        G.append(num_list[i])
        answer+=num_list[i]

    if num_list[i]-num_list[i-1]==1:
        G.append(num_list[i])

    else:
        if i != 0:  
            answer+=num_list[i]

print(answer)        