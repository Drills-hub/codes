def solution(s):
    count = 0
    remove_0_total = 0
    answer = []

    while s != "1":
        remove_0 = 0
        count += 1
        s_len = len(s)
        remove_0 += s.count("0")
        remove_0_total += remove_0
        new_s = s_len - remove_0
        s = bin(new_s)[2:]

    answer.append(count)
    answer.append(remove_0_total)
    return answer