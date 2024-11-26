def oven_alarm(x, y):
    h = int(x[0])
    m = int(x[1])
    h_cook = int(y) // 60
    m_cook = int(y) % 60
    answer_h = h + h_cook
    answer_m = m + m_cook

    if answer_m > 59:
        answer_h = answer_h + 1
        answer_m = answer_m - 60

    if answer_h > 23:
        answer_h = answer_h - 24

    return " ".join([str(answer_h), str(answer_m)])


a_time = input().split()
cook_m = input()

print(oven_alarm(a_time, cook_m))