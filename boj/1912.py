n = int(input())
data = list(map(int, input().split()))
dp = []
csum = 0

for num in data:
    csum = csum + num
    dp.append(csum)
    if(csum < 0):
        csum = 0
  
print(max(dp))
