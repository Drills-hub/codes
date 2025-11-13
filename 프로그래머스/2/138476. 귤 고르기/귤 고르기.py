def solution(k, tangerine):
    count_dict = {}
    for t in tangerine:
        if t in count_dict:
            count_dict[t] += 1
        else:
            count_dict[t] = 1

    sorted_counts = sorted(count_dict.values(), reverse=True)
    
    total = 0
    answer = 0
    
    for cnt in sorted_counts:
        total += cnt
        answer += 1
        if total >= k:
            return answer

    return answer