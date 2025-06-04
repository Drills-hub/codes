x,y = map(int,input().split()) 

def repunit_num(n):
    result = ["1"] * n
    result_str = "".join(result)
    return int(result_str)

answer = repunit_num(x) + repunit_num(y)
print(answer)