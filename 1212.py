N = input()[::-1]
cnt = 1
dec = 0
ans = ''

# 8진수 -> 10진수
for i in N:
    dec += int(i) * cnt
    cnt *= 8

# 10진수 -> 2진수
if(dec == 0):
    print(0)
else:
    while(dec > 0):
        if(dec % 2 == 0):
            ans += '0'
        else:
            ans += '1'
        dec //= 2
    print(ans[::-1])

#print(bin(int(input(),8))[2:])