A=input()
B=input()

i = 0
count = 0
while i <= len(A) - len(B):

    if A[i:i+len(B)] == B:
        count += 1
        i += len(B)
    else:
        i += 1

print(count)