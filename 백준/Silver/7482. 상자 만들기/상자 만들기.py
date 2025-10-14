import sys

def test(a: float) -> float:
    return a / 6

n = int(sys.stdin.readline())
for _ in range(n):
    a = float(sys.stdin.readline())
    b = test(a)
    print(f"{b:.10f}")