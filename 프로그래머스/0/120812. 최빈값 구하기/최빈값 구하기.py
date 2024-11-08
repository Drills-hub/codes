from collections import Counter

def solution(array):
    modes = []
    counter = Counter(array)
    max_count = max(counter.values())
    
    for i, j in counter.items():
        if j == max_count:
            modes.append(i)
    
    if len(modes) > 1:
        return -1
    else:
        return modes[0]
    