import sys

bug_code = sys.stdin.read()

while "BUG" in bug_code:
    bug_code = bug_code.replace("BUG", "")

print(bug_code, end="")