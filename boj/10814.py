num = set([i for i in range(1,10001)])
generator = set([])

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generator.add(i)

self_num = sorted(num - generator)
for snum in self_num:
    print(snum)