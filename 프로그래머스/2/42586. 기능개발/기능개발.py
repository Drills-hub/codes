def solution(progresses, speeds):
    answer = []
    days = []

    for i in range(len(progresses)):
        progress = 100 - progresses[i]
        per_day = progress // speeds[i]

        if progresses[i] + (speeds[i] * per_day) >= 100:
            days.append(progress // speeds[i])
        else:
            days.append((progress // speeds[i]) + 1)

    count = 1
    current_max = days[0]

    for j in range(1, len(days)):
        if days[j] <= current_max:
            count += 1
        else:
            answer.append(count)
            current_max = days[j]
            count = 1

    answer.append(count)
    return answer