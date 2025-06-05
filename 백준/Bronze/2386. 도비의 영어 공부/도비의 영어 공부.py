while True:
    str_input = input().split()
    if str_input[0]== '#':
        break
    
    count = 0
    for i in range(1,len(str_input)):
        for j in str_input[i]:
            j = j.lower()
            if j == str_input[0]:
                count += 1
        
    print(str_input[0],count)