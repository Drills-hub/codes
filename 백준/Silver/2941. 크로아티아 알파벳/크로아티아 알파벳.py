def solution(word):
    croatia_alphabet = ["c=", "c-", "d-", "lj", "nj", "s=", "dz=", "z="]
    
    for i in croatia_alphabet:
        word = word.replace(i, "1")
    return len(word)


word = input()
print(solution(word))
