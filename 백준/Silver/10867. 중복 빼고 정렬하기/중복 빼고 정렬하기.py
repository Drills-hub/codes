n = int(input())
num = list(map(int, input().split()))

de_duplication_num = sorted(set(num))
print(" ".join(map(str, de_duplication_num)))