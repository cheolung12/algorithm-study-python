n = int(input())
s = 2

while(n != 1):
    while (n % s == 0):
        n = n // s
        print(s)
    s += 1


