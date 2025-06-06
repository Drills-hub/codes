x, y= map(int, input().split())

def factorial(x):
    n=1
    for i in range(2,x+1):
        n*=i
    return n

n=factorial(x)
k=factorial(y)
n_k=factorial(x-y)

result=n//(k*n_k)

print(result)