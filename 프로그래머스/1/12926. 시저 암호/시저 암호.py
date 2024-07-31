"""
문제 이해
주어지는 문자열 s 를 n 만큼 밀어서
다른 알파벳으로 만드는 시저암호 함수를 만들어라.

조건
공백은 아무리 밀어도 공백입니다.
s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
s의 길이는 8000이하입니다.
n은 1 이상, 25이하인 자연수입니다.

코드 설계
1. 문자열 s와 밀어낼 자연수 n 을 받아서  활용
2. 문자열을 아스키 코드를 이욯해서 숫자로 바꾼다.
3. 그 수에  n을 더하고 문자로 바꿈
4. 바꾼 문자를 하나의 문자열로 출력
"""


def solution(s, n):
    cc = []
    for i in s:
        # 빈칸도 아스키 코드로 변환 되기때문에
        if i == " ":
            cc.append(" ")
        # 아스키 코드 안에서 대문자를 출력하기 위해
        else:
            i_num = ord(i)
            if 123 > i_num > 96:
                if i_num + n > 122:
                    j = (i_num + n) - 122
                    cc_word = chr(96 + j)
                    cc.append(cc_word)
                else:
                    cc_word = chr(i_num + n)
                    cc.append(cc_word)
            # 아스키 코드 안에서 소문자를 출력하기 위해
            elif 91 > i_num > 64:
                if i_num + n > 90:
                    j = (i_num + n) - 90
                    cc_word = chr(64 + j)
                    cc.append(cc_word)
                else:
                    cc_word = chr(i_num + n)
                    cc.append(cc_word)
            else:
                cc_word = chr(i_num + n)
                cc.append(cc_word)
    result = ''.join(cc)
    return result