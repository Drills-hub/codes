def quadrant(x,y):
    if x > 0 and y > 0:
        return print(1)
    elif x < 0 and y > 0:
        return print(2)
    elif x < 0 and y < 0:
        return print(3)
    elif x > 0 and y < 0:
        return print(4)

x = int(input())
y = int(input())
quadrant(x,y)