"""
코드 설계
1.combinations 라이브러리와 for문을 사용해서 
두 수씩 짝짓기
2.두 수를 더한 값을 answer 리스트에 중복 없을 경우 추가
3. 완성된 answer리스트를 오름차순으로 정렬 후 리턴 
"""

from itertools import combinations
n = [2,1,3,4,1]

def solution(n):
    answer = []
    for i in combinations(n,2) :
        sum_n = sum(i)
        if sum_n not in answer:
            answer.append(sum_n)
        
        
    return sorted(answer)

