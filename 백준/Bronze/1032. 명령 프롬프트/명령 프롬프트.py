n = int(input())
pattern_list = []

for _ in range(n):
    pattern_list.append(input())

answer = list(pattern_list[0])

for i in range(1, n): 
    for j in range(len(answer)):  
        if j < len(pattern_list[i]) and answer[j] != pattern_list[i][j]:
            answer[j] = "?"  

answer = ''.join(answer)  
print(answer)