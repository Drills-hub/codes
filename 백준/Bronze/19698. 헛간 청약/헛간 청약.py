n,w,h,l= map(int,input().split())

W = w//l
H = h//l

answer = (W*H)
if answer < n:
    print(answer)
else:
    print(n)