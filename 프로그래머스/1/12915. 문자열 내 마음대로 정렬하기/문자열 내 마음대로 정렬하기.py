def solution(strings, n):
    #리스트 정렬하기(sort에 키값을 이용해서 문자열 x의 n번째 글자를 기준으로 정렬)
    strings.sort(key=lambda x: (x[n], x))
    # 정렬된 리스트 값 리턴
    return strings


