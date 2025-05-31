def student_id(S):
    H = 508 
    G = 108 
    E = 212 
    I = 305 
    POSTAL_CODE = 4763  
    
    results = []
    
    # 해당없음 
    if S % POSTAL_CODE != 0:
        print(0)
        return
    
    quotient = S // POSTAL_CODE
    
    # 가능한 모든 a, b 쌍 찾기 (a: 국어-영어 차이, b: 수학-탐구 차이)
    # a와 b의 범위는 0에서 200까지
    for a in range(0, 201):
        for b in range(0, 201):
            # 가능한 4가지 경우의 수 확인
            
            # 경우 1: 국어 > 영어, 수학 > 탐구
            if a * H + b * E == quotient:
                results.append((a, b))
            
            # 경우 2: 국어 > 영어, 수학 <= 탐구
            if a * H + b * I == quotient and (a, -b) not in results:
                results.append((a, -b))
            
            # 경우 3: 국어 <= 영어, 수학 > 탐구
            if a * G + b * E == quotient and (-a, b) not in results:
                results.append((-a, b))
            
            # 경우 4: 국어 <= 영어, 수학 <= 탐구
            if a * G + b * I == quotient and (-a, -b) not in results:
                results.append((-a, -b))
    
    # 중복 제거 및 정렬
    results = sorted(list(set(results)), key=lambda x: (abs(x[0]), abs(x[1])))
    
    # 결과 출력
    print(len(results))
    for a, b in results:
        print(abs(a), abs(b))

# 입력 받기
S = int(input().strip())
student_id(S)