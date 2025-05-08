N = int(input())
x,y = 0,0
while N > 0:
    winner = input()
    if winner == "D":
        x += 1
    elif winner == "P":
        y += 1
    N -= 1
    if abs(x-y) == 2:
        break
    
print(f"{x}:{y}")    