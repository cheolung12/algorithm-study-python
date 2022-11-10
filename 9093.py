import sys

n = int(sys.stdin.readline())

for i in range(n):
    data = sys.stdin.readline().split()
    for j in range(len(data)):
        data[j] = data[j][::-1]
    print(*data)
    data.clear()
    