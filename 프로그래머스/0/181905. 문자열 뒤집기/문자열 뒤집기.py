def solution(my_string, s, e):
    my_string_split = my_string[s : e + 1]
    reversed(my_string_split)
    answer = (
        my_string[0:s] + "".join(list(reversed(my_string_split))) + my_string[e + 1 :]
    )
    return answer