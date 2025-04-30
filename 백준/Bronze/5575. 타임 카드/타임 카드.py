for i in range(3):
    a,b,c,d,e,f, = map(int, input().split())
    s=f-c
    if s<0:
        s+=60
        e-=1
    m=e-b
    if m<0:
        m+=60
        d-=1
    h=d-a
    print(h,m,s)
   