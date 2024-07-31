"""
문제 이해

주어지는 2차원 배열 size를 매개변수로
모든 명함을 넣을 수 있는 가장 작은 지갑 크기 구하기

코드 설계
1.가로 중 가장 큰 수와 세로중 가장 큰 수를 찾기
2 두 수를 곱한 값을 출력
"""

def solution(sizes):
    #가로세로 상관없음
    width = []
    height = []
     # 주어진 2차원 배열 수만큼 반복
    for i in range (len(sizes)):
         # 배열 내에 큰 수와 작은 수 구분
        width.append(max(sizes[i]))
        height.append(min(sizes[i]))
         # 두 수 곱하기
    result = max(width)*max(height)
    return result