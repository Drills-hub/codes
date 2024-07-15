def solution(absolutes, signs):
    num_sum = 0
    for num, sign in zip(absolutes, signs):
        if sign == True:
            num_sum += num
        else:
            num_sum += -1*num

    return num_sum