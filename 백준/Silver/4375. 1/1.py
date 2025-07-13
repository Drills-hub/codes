while True:
    try:
        n = int(input())
    except:
        break

    answer = 0
    count = 1
    while True:
        answer = answer * 10 + 1
        answer %= n
        if answer == 0:
            print(count)
            break
        count += 1