"""
문제 이해

number = 정수 배열

3 <= number <=14

배열에서 3개의 정수를 더했을때 
0이 나오는 경우의 수를 구하는 함수를 만들어라

코드 설계 

3개 씩 묶을 수 있는 모든 경우의 수를 구하기

그 중에 더했을 때 1이 나오는 경우를 카운트 하기
"""

def solution(number):
    count = 0
    n = len(number)
    # 3중 for 루프로 모든 가능한 세 학생의 조합을 생성
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # 각 조합의 합이 0이면 카운트 증가
                if number[i] + number[j] + number[k] == 0:
                    count += 1
    return count