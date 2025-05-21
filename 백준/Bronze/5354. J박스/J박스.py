n = int(input())
for idx in range(n):  
    j = int(input())
    for i in range(j):
        if i == 0 or i == j-1:
            print("#"*j) 
        else:   
            print("#" + "J"*(j-2) + "#")
    if idx != n-1: 
        print()