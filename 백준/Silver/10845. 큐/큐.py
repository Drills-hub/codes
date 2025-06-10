import sys
input = sys.stdin.readline

n = int(input())
queue_list = []

for i in range(n):
    command_word = input().split()

    if command_word[0] == "push":
        queue_list.append(command_word[1])
    elif command_word[0] == "pop":
        if queue_list:
            print(queue_list.pop(0))
        else:
            print(-1)
    elif command_word[0] == "size":
        print(len(queue_list))
    elif command_word[0] == "empty":
        if queue_list:
            print(0)
        else:
            print(1)
    elif command_word[0] == "front":
        if queue_list:
            print(queue_list[0])
        else:
            print(-1)
    elif command_word[0] == "back":
        if queue_list:
            print(queue_list[-1])
        else:
            print(-1)