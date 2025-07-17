n=int(input())
answer=0

for _ in range(n):
    vote=int(input())
    answer+=vote

if answer>n/2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")