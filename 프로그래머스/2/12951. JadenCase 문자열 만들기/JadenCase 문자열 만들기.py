def solution(s):
    s_list = s.lower().split(" ")
    JadenCase = []
    
    for word in s_list:
        if word:  
            JadenCase.append(word[0].upper() + word[1:])
        else:
            JadenCase.append("")

    return " ".join(JadenCase)
