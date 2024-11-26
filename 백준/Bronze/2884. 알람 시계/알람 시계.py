def alarm(x):
    i = int(x[0])
    j = int(x[1])

    if j - 45 < 0:
        if i - 1 < 0:
            i = 23
            m = 60 + (j - 45)
        else:
            i = i - 1
            m = 60 + (j - 45)
    else:
        m = j - 45

    return " ".join([str(i), str(m)])


a_time = input().split()
print(alarm(a_time))