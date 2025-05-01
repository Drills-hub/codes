def count_max_lowercase(s):
    count_dict = {}
    
    for char in s:
        if char.islower():
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
    
    max_count = max(count_dict.values())
    return max_count



N = int(input())
string = input()

print(count_max_lowercase(string))