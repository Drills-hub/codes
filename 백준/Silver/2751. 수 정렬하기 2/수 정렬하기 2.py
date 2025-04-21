import sys
input = sys.stdin.readline

N = int(input())
result = [int(sys.stdin.readline()) for _ in range(N)]
result.sort()
sys.stdout.write('\n'.join(map(str, result)) + '\n')