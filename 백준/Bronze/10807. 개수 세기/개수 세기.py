def solution(N):

    list_array = input().split()
    v = input()

    count = list_array.count(v)

    return count


N = int(input())
print(solution(N))