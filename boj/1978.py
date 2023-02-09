n = int(input())
ans = []
li = list(map(int, input().split()))

for num in li:
    if(num == 1):
        continue
    for i in range(2,num):
        if(num % i == 0):
            break
    else: ans.append(num)

print(len(ans))


        