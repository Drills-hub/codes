import sys
input = sys.stdin.readline

def solution(cmd, S):
    if cmd[0] == "add":
        S.add(int(cmd[1]))
    elif cmd[0] == "remove":
        if int(cmd[1]) in S:
            S.remove(int(cmd[1]))
    elif cmd[0] == "check":
        if int(cmd[1]) in S:
            print(1)
        else:
            print(0)
    elif cmd[0] == "toggle":
        if int(cmd[1]) in S:
            S.remove(int(cmd[1]))
        else:
            S.add(int(cmd[1]))
    elif cmd[0] == "all":
        S.clear()
        S.update({i for i in range(1, 21)})
    elif cmd[0] == "empty":
        S.clear()


N = int(input())
S = set()
for i in range(N):
    cmd = input().split()
    solution(cmd, S)