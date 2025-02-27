answer=[]
def factor_n_multiple(N,M):
    if N % M == 0: 
        answer.append("multiple")
    elif M % N == 0:
        answer.append("factor")
    else:
        answer.append("neither")

while True:
    N,M=map(int,input().split())
    if N==0 and M==0:
        break
    else:
        factor_n_multiple(N,M)

print('\n'.join(answer))