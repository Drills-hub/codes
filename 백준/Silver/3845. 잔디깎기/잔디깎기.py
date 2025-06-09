def is_covered(road, l, w):
    road = sorted(road)
    covered = 0.0

    for p in road:
        left = p - w / 2
        right = p + w / 2

        if left <= covered:
            covered = max(covered, right)
        else:
            return False
    return covered >= l

while True:
    x, y, z = input().split()
    x = int(x)
    y = int(y)
    z = float(z)

    if x == 0 and y == 0 and z == 0.0:
        break

    x_list = list(map(float, input().split()))
    y_list = list(map(float, input().split()))

    horizontal_ok = is_covered(x_list, 75.0, z)
    vertical_ok = is_covered(y_list, 100.0, z)

    if horizontal_ok and vertical_ok:
        print("YES")
    else:
        print("NO")