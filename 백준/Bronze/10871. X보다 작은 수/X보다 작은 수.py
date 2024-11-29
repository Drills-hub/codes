def solution(N, X):
    
    list_array = list(map(int, input().split()))
    return " ".join([str(num) for num in list_array if num < X])

N, X = map(int, input().split())
print(solution(N, X))
