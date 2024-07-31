word= input().strip().split()

def len_word(word):
    word_str = ''.join(word)
    cnt = len(word_str)
    return cnt

print(len_word(word))