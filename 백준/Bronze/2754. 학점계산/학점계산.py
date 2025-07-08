grade=input()
answer=0
for i in grade:         
    if i == 'A':
        answer+=4.0
    elif i == 'B':
        answer+=3.0
    elif i == 'C':
        answer=2.0
    elif i == 'D':
        answer=1.0
    elif i == 'F':
        answer=0.0
    if i == '+':
        answer+=0.3
    if i == '-':
        answer-=0.3

print(answer)