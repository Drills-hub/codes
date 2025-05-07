N = int(input())
Vote = list(map(int,input().split()))
Vote_set = set(Vote)

count = {}
for i in Vote_set:
    count[i] = Vote.count(i)

max_value = max(count.values())
answer = []
for i in count:
    if i== 0:
        continue
    elif count[i] == max_value:
        answer.append(i)

if len(answer) > 1:
    print("skipped")
else:
    print(answer[0])