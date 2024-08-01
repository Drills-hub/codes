"""
문제 이해
문자열 s는 숫자를 뜻하는 영단어와 숫자로 이루어져있다.
s를 원래의미하는 숫자로 출력하라.

조건
1<=len(s)<=50
s는 0 or 'zero'로 시작하지 않는다.
return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어진다.

코드 설계
1.문자열에 있는 영단어를 찾는다.
2.영단어를 숫자로 바꾼다.
3 완성된 숫자를 출력한다.
"""

def solution(s):
    num = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in num:
        if i in s:
            s = s.replace(i, str(num.index(i)))
    return int(s)