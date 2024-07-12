def solution(x):
    h = [int(h) for h in str(x)]
    si= sum(h)
    if x % si == 0:
        return True
    else: return False