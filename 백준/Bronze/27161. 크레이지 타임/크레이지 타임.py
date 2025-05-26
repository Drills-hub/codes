n = int(input())

clock = 0
direction = 1

for _ in range(n):
    x, y = input().split()
    y = int(y)
    
    clock += direction
    
    if clock == 0:
        clock = 12
    elif clock > 12:
        clock = 1
    elif clock < 1:
        clock = 12
    
    
    if x == "HOURGLASS":
        if y == clock:
            print(clock, "NO")
        else:
            direction *= -1 
            print(clock, "NO")
    else:
        print(clock, "YES" if y == clock else "NO")