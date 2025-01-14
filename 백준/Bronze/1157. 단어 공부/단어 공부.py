S = input().upper()
char_counts = {}

for char in S: 
    char_counts[char] = char_counts.get(char, 0) + 1

max_count = 0
max_count_char = ''
duplicates = 0

for char, count in char_counts.items():
    if count > max_count:
        max_count = count
        max_count_char = char
        duplicates = 0
    elif count == max_count:
        duplicates += 1

if duplicates >= 1:
    print("?")
else:
    print(max_count_char)