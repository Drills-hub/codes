#일단 행렬 입력 받아서 저장해야함.행을 9번 나눠 받는다.
def make_matrix():
    matrix = []
    for _ in range(9):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix



# 행별로 최대값 찾아서 그 중 가장 큰값  출력
def max_num(n):
    max_num_list = []
    for i in range(9):
        row = max(n[i])
        max_num_list.append(row)
        result = max(max_num_list)
    return  result

#최댓값의 위치 찾기
def position(n,m):
    for i in range(9):
        for j in range(9):
            if n[i][j] == m:
                return  f"{i+1} {j+1}"


matrix_a = make_matrix()
max_num_a = max_num(matrix_a)
position_a= position(matrix_a,max_num_a)

print(max_num_a)
print(position_a)