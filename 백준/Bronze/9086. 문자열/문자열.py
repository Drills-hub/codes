
T = int(input().strip())

def first_last():
    for i in range(T):
        word = input().strip().split()
        word_str = ''.join(word)
        print(word_str[0]+word_str[-1])

first_last()