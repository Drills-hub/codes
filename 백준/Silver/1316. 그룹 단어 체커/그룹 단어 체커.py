n = int(input())
result = 0
for i in range(n):
    w = input()
    if list(w) == sorted(w, key=w.find):
        result += 1
print(result)