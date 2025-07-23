def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

a, b= map(int, input().split())
new_num= a+(b*10**len(str(a)))

if is_prime(new_num) and is_prime(a):
    print("Yes")
else:
    print("No")