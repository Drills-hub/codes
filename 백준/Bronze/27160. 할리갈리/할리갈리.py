n = int(input())

HalliGalli = {"STRAWBERRY": 0, "BANANA": 0, "LIME": 0, "PLUM": 0}
for i in range(n):
    fruit, x = input().split()
    HalliGalli[fruit] += int(x)

if HalliGalli.get("STRAWBERRY", 0) == 5 or HalliGalli.get("BANANA", 0) == 5 or HalliGalli.get("LIME", 0) == 5 or HalliGalli.get("PLUM", 0) == 5:
    print("YES")
else:
    print("NO")