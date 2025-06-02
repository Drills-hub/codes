def find_N(P1, P2, P3, X1, X2, X3):
    n = X1
    max_try = P1 * P2 * P3  
    while n < X1 + max_try:
        if n % P2 == X2 and n % P3 == X3:
            return n
        n += P1
    return -1  

P1, P2, P3, X1, X2, X3 = map(int, input().split())
result = find_N(P1, P2, P3, X1, X2, X3)
print(result)