"""
코드 설계
1. food를 인덱스와 함께 묶어 딕셔너리로 저장
2. food의 숫자가 1보다 커야만 answer에 추가
3.물은 항상 1개이고 가운데 이기때문에 따로 추가한 후 역순의 answer을 추가
"""

def solution(foods):
    answer = []
    idx = {}
    for i, food in enumerate(foods):
        if food > 1:
            cnt = food//2
            for _ in range(cnt):
                answer.append(i)

    answer_str = ''.join(map(str, answer + [0] + answer[::-1]))
    return answer_str

