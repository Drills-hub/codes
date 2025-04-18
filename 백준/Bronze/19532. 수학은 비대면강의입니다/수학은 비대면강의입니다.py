a,b,c,d,e,f = map(int, input().split())

y = (a*f-c*d)//(a*e-d*b)
x = (c*e-b*f)//(a*e-d*b)

print(x,y)