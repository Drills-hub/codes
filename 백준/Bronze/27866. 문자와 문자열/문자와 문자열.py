
"""
문제 이해
단어 S와 정수 i가 주어졌을 때,
S의 i번째 글자를 출력하는 프로그램을 작성

조건
영어 소문자와 대문자로만 이루어진 단어 S(길이는 최대 1000)
정수 i  (1<=i<=|S|)

코드 설계
1. 단어 S와 정수 i를 입력 받기
2.단어 S를 문자열로 변환하기
3.문자열 S[i-1]를 출력하기

"""
S = input().strip()
i = int(input().strip())

def str_sl(s,i):
    print(s[i-1])


str_sl(S,i)