S=input()

def is_ucpc(s):
    target = 'UCPC'
    idx = 0
    for char in s:
        if char == target[idx]:
            idx += 1
            if idx == len(target):
                return True
    return False

if is_ucpc(S):
    print("I love UCPC")
else:
    print("I hate UCPC")