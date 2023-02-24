n = int(input())

def hanoi(n, start, mid, dest):
    if n == 1:
        print(start, dest)
    else:
        hanoi(n-1,start, dest, mid)
        print(start, dest)
        hanoi(n-1, mid, start, dest)

print(2**n-1) # 2의n승 - 1 (하노이탑 이동횟수)
hanoi(n,1,2,3)