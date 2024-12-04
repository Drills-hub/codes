def solution():
    attendance = []
    answer = []

    for _ in range(28):
        N = input()
        attendance.append(N)

    for i in range(1, 31):
        if str(i) not in attendance:  
            answer.append(i)
    answer.sort()  

    return " ".join(map(str, answer))  

print(solution())