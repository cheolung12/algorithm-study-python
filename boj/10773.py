# n = int(input())
# numbers = []
# for _ in range(n):
#     num = int(input())
#     if num == 0:
#         numbers.pop()
#     else: 
#         numbers.append(num)
# print(sum(numbers))
# 왜 시간초과지..??

n = int(input())
z = []
for i in range(n):
    num = int(input())
    if num == 0:
        z.pop()
    else:
        z.append(num)
print(sum(z))