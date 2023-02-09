import sys

voca = sys.stdin.readline().rstrip()
result = [0] * 26

for alpha in voca:
    result[ord(alpha) - ord('a')] += 1

print(*result)
