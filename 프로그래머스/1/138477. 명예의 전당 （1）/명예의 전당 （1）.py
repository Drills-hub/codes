"""
코드 설계
1.score의 원소들을 for문으로 돌리면서 k_list에 추가
2.두가지 경우로 나눠 k보다 작을 경우 현재 k_list의 제일 작은 값을 rlt에 추가
  k보다 클 경우 k_list를 내림차순 정렬헤 k-1번째 수를 rlt에 추가
3.rlt 값 리턴
"""
def solution(k, score):
    rlt = []
    k_list=[]
    for i in score:
        #k보다 작을 경우
        if len(k_list) < k:
            k_list.append(i)
            rlt.append(min(k_list))
        #k보다 클 경우
        else:
            k_list.append(i)
            k_list.sort(reverse=1)
            rlt.append(k_list[k-1])
    
        
    return rlt