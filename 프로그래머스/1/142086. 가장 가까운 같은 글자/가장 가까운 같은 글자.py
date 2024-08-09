
"""
코드 설계
1. 문자열을 하나씩 나눠 인덱스와 알파벳을 따로 딕셔너리로 저장
2. 문자열을 글자 하나 씩 비교해서 
   앞에 같은 글자가 있었는지 확인
3. 앞에 없으면 -1, 있으면 인덱스를 비교해서 숫자 변환
4. 결과값 출력

"""
def solution(s):
    answer = []
    idx = {}

    for i, j in enumerate(s):
        #알파벳이 이미 인덱스에 있다면
        if j in idx:
            dif = i - idx[j] + 1
            answer.append(dif)
            idx[j] = i + 1
        #알파벳이 처음 나왔다면
        else:
            answer.append(-1)
            idx[j] = i + 1

    return answer