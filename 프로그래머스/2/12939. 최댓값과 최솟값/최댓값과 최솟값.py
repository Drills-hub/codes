def solution(s):
    num_list = []
    num = list(map(int, s.split()))
    num_list.append(min(num))
    num_list.append(max(num))

    return ' '.join(map(str,num_list))