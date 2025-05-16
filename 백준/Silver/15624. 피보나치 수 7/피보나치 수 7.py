def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    prev_num = 0
    prev_num2 = 1
    for _ in range(2, n + 1):
        current = (prev_num + prev_num2) % 1000000007
        prev_num = prev_num2
        prev_num2 = current
    return prev_num2

n = int(input())
print(fibo(n))