def muti_sum(num):
    answer = []
    for _ in range(num):
        x, y = map(int, input().split())
        answer.append(x + y)
    print("\n".join(map(str, answer)))


num = int(input())
muti_sum(num)