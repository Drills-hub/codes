import sys,math
input = sys.stdin.readline

r = int(input())

a = format( math.pi*r**2, '.6f')
b = format(2 * r**2, '.6f')

print(a)
print(b)