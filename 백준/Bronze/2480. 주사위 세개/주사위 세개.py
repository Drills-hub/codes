def dice(rewords):
    if rewords[0] == rewords[1] == rewords[2]:
        print(10000 + rewords[0] * 1000)

    elif rewords[0] == rewords[1] or rewords[0] == rewords[2]:
        return print(1000 + rewords[0] * 100)

    elif rewords[1] == rewords[2]:
        return print(1000 + rewords[1] * 100)

    else:
        print(max(rewords) * 100)


rewords = list(map(int, (input().split())))
dice(rewords)