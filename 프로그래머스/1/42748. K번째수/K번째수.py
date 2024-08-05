def solution(array, commands):
    answer = []
    for command in commands:
        # 언패킹을 이용해서 값 할당
        start, end, k = command
        # array의 서브리스트를 추출하고 정렬(이때 start는 인덱스 기반 이므로 -1)
        sorted_array = sorted(array[start-1:end])
        # k번째 요소를 추가 (k는 1 기반 인덱스이므로 k-1)
        answer.append(sorted_array[k-1])
    return answer