import sys
input = sys.stdin.readline

n = int(input())
couples = {} 
ring_types = set()  
is_couples = []  

for _ in range(n):
    name, ring = input().split()
    if ring == '-':
        continue
    else:
        couples[name] = ring
        ring_types.add(ring)

for ring in ring_types:
    count = 0
    
    for ring_name in couples.values():
        if ring_name == ring:
            count += 1
    if count == 2:  
        is_couples.append(ring)

print(len(is_couples)) 

for ring in is_couples:
    pair = []
    for name, r in couples.items():
        if r == ring:
            pair.append(name)
    print(pair[0], pair[1])