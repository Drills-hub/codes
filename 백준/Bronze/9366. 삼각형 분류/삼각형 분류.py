t=int(input())

for i in range(1,t+1):
    triangle=list(map(int,input().split()))
    triangle.sort(reverse=True)

    if triangle[0] >= triangle[1] + triangle[2]:
        print(f"Case #{i}: invalid!")
    else:
        if triangle[0]==triangle[1]==triangle[2]:
            print(f"Case #{i}: equilateral")
        elif triangle[0]==triangle[1] or triangle[0]==triangle[2] or triangle[1]==triangle[2]:
            print(f"Case #{i}: isosceles")
        else:
            print(f"Case #{i}: scalene")