data = input()
li = []
for i in range(len(data)):
    li.append(data[i:])

for i  in sorted(li):
    print(i)