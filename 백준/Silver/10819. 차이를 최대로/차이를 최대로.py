import itertools,sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
    
max_num = 0
    
for permutation in itertools.permutations(A):
    current_sum = 0
    for i in range(N - 1):
        current_sum += abs(permutation[i] - permutation[i+1])
    
    max_num = max(max_num, current_sum)
print(max_num)