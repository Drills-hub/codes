# 5행 n열 행렬 만들기
def make_matrix():
    matrix = []
    for _ in range(5):
        row = input()
        matrix.append(row)
    return matrix

# 행렬을 세로로 읽게 만들기
def read_column(matrix):
    for j in range(15):
        for i in range(5):
            if j < len(matrix[i]):
                print(matrix[i][j], end='')
    print()


matrix_a = make_matrix()
read_column_a = read_column(matrix_a)
