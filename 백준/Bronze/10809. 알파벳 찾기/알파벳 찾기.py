def solution(S):
    answer = {}

    for i, char in enumerate(S):
        if char not in answer:
            answer[char] = i

    result = []
    for char in range(ord("a"), ord("z") + 1):
        result.append(answer.get(chr(char), -1))

    return " ".join(map(str, result))


S = input()
print(solution(S))