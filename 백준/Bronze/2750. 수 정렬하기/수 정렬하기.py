import sys

N = int(sys.stdin.readline())
answer = [int(sys.stdin.readline()) for _ in range(N)]
answer.sort()
sys.stdout.write('\n'.join(map(str, answer)) + '\n')