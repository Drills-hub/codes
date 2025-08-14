import sys

input = sys.stdin.readline

B, C, D = map(int, input().split())

berger_price = sorted(list(map(int, input().split())), reverse=True)
sides_price = sorted(list(map(int, input().split())), reverse=True)
juice_price = sorted(list(map(int, input().split())), reverse=True)


total = sum(berger_price) + sum(sides_price) + sum(juice_price)
discounted_total = 0


for i in range(max(B, C, D)):
    count = 0
    if i < len(berger_price):
        count += 1
    if i < len(sides_price):
        count += 1
    if i < len(juice_price):
        count += 1
    if count == 3:
        discounted_total += berger_price[i] * 0.9
        discounted_total += sides_price[i] * 0.9
        discounted_total += juice_price[i] * 0.9
    else:
        if i < len(berger_price):
            discounted_total += berger_price[i]
        if i < len(sides_price):
            discounted_total += sides_price[i]
        if i < len(juice_price):
            discounted_total += juice_price[i]

print(total)
print(int(discounted_total))