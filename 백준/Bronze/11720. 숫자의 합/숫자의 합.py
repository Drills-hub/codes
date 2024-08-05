"""
코드 설계
1. 문자열의 len을 N으로 입력 받고, 공백 없는 숫자열을 num_str로 입력 받는다.
2.문자열의 인덱스를 이용해서  숫자열을 하나씩 슬라이싱해서 nums리스트화 한다.
3.리스트를 sum 하고, 출력한다.
"""

N = int(input().strip())
num_str = input().strip()
def sum_nums():
    nums = []
    for i in range(N):
        nums.append(int(num_str[i]))
    result = sum(nums)
    return result


a = sum_nums()
print(a)