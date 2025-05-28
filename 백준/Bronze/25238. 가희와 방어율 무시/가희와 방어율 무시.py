a,b=map(int,input().split())    

shield=a*(100-b)//100
if shield<100:
    print(1)
else:
    print(0)