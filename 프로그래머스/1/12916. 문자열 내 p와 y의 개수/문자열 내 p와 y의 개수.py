def solution(s):

    a = s.lower().count("p")
    b = s.lower().count("y")

    if a == b:
        return True
    else:
        return False

