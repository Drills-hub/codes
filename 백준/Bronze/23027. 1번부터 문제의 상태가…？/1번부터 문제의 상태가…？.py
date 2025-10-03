s= input()
answer=list(s)

if 'A' in answer:
    for i in range(len(answer)):
        if answer[i] in ['B', 'C', 'D', 'F']:
            answer[i] = 'A'
elif 'B' in answer:
    for i in range(len(answer)):
        if answer[i] in ['C', 'D', 'F']:
            answer[i] = 'B'
elif 'C' in answer:
    for i in range(len(answer)):
        if answer[i] in ['D', 'F']:
            answer[i] = 'C'
else:
    for i in range(len(answer)):
        answer[i] = 'A'

print(''.join(answer))  