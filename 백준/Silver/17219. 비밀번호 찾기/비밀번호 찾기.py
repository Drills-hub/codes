import sys
input=sys.stdin.readline

N,M=map(int,input().split())

site_password=dict()
for _ in range(N):
    site,password=input().split()
    site_password[site]=password

for _ in range(M):
    site=input().rstrip()
    print(site_password[site])