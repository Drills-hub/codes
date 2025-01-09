score_map = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

score_list = []
sum_score = 0

for _ in range(20):
    test_score = input().split()
    grade = test_score[-1]
    credit = float(test_score[1])

    if grade in score_map:
        score_list.append(score_map[grade] * credit)
        sum_score += credit

answer = round((sum(score_list) / sum_score), 6)

print(f"{answer:.6f}")