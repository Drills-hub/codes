n=int(input())

for _ in range(n):
    score=0
    life=input().strip()
    for i in life:
        if 'A' <= i <= 'Z':  
            score += ord(i)-64
    if score == 100:
        print("PERFECT LIFE")
    else:   
        print(score)