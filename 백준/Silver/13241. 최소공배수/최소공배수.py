A, B = map(int, input().split())
a, b = A, B  
while B:
    A, B = B, A % B
print((a * b) // A)