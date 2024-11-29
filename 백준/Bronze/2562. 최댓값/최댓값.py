def solution():
    num_list=[]
    idx=0
    for _ in range(9):
        N = int(input())
        num_list.append(N)
    for i in range(len(num_list)):
        if max(num_list)==num_list[i]:
            idx+=i+1


    return f"{max(num_list)}\n{idx}"


print(solution())