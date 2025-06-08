def count_atom(n,e):
    atom_list = list(map(int,input().split()))
    atom_list.sort(reverse=True)
    count = 1
    for i in range(n-1):
        if atom_list[i] - atom_list[i+1] < e:
            continue
        else:
            count += 1
    return count

n,e = map(int,input().split())
print(count_atom(n,e))