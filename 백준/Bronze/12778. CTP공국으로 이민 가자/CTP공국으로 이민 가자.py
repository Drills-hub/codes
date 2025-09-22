T = int(input())

for _ in range(T):
    M, mode = input().split()
    if mode == "C":
        characters = input().split()
        answer = []
        for char in characters:
            answer.append(str(ord(char) - 64))
    else:
        numbers = list(map(int, input().split()))
        answer = []
        for num in numbers:
            answer.append(chr(num + 64))

    print(" ".join(answer))