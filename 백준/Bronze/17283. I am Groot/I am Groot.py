def loop(L, R):

    total_length = 0
    branch_length = L
    count = 0
    
    while True:
        branch_length = int(branch_length * (R / 100))
        count += 1
        num_branches = 2 ** count
        if branch_length <= 5:
            break
        
        total_length += branch_length * num_branches
        
    return total_length

L = int(input())
R = int(input())
result = loop(L, R)
print(result)