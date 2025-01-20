N,M =map(int,input().split())

A=[]
B=[]

for _ in range(N):
    i = list(map(int,(input().split())))
    A.append(i)

for _ in range(N):
    j = list(map(int,input().split()))
    B.append(j)
    

for x in range(N):
    row = []
    for y in range(M):
        V = A[x][y]+ B[x][y]
        row.append(str(V))
    print(' '.join(row))
