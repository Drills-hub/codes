n = int(input())
for _ in range(n):
    name = input().strip()
    lower_name = name.lower()
    g_count = lower_name.count('g')
    b_count = lower_name.count('b')
    
    result = ""
    if g_count > b_count:
        result = "GOOD"
    elif g_count < b_count:
        result = "A BADDY"
    else:
        result = "NEUTRAL"
    
    print(f"{name} is {result}")