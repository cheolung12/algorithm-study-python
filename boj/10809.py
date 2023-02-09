import sys

voca = sys.stdin.readline().rstrip()
result = [-1] * 26

for i in range(len(voca)):
    if(result[ord(voca[i]) - ord('a')] == -1):
        result[ord(voca[i]) - ord('a')] = i
    

print(*result)
