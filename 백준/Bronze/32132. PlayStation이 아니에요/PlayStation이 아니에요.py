import sys
input = sys.stdin.readline

N = int(input().strip())
ps_str  = input()

while "PS4" in ps_str or "PS5" in ps_str :
    ps_str = ps_str .replace("PS4", "PS").replace("PS5", "PS")

print(ps_str)  