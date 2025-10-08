import sys

input = sys.stdin.readline

n = int(input())
students = []
for _ in range(n):
    students.append(input().split())

students.sort(
    key=lambda student: (
        -int(student[1]),
        int(student[2]),
        -int(student[3]),
        student[0],
    )
)
for student in students:
    print(student[0])