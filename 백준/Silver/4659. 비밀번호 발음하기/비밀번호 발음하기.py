def valid_vowel_word(word):
    valid = ["a", "e", "i", "o", "u"]
    for i in valid:
        if i in word:
            return True
    return False

def valid_double_word(word):
    for i in range(len(word) - 1):
        if word[i] == "e" and word[i + 1] == "e":
            return True
        if word[i] == "o" and word[i + 1] == "o":
            return True
        elif word[i] == word[i + 1]:
            return False
    return True

def valid_succession_word(word):
    vowels = 'aeiou'
    word = word.lower()
    
    for i in range(len(word) - 2):
        current = word[i:i+3]
        all_vowels = True
        for c in current:
            if c not in vowels:
                all_vowels = False
                break
        all_consonants = True
        for c in current:
            if c in vowels or not c.isalpha():
                all_consonants = False
                break
        
        if all_vowels or all_consonants:
            return False
    return True

while True:
    word = input()
    if word == "end":
        break

    if valid_vowel_word(word) and valid_succession_word(word) and valid_double_word(word) and valid_succession_word(word):
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")