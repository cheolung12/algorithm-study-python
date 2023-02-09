N = input()[::-1]
ans = ''
tmp = 0
cnt = 1

for i in N:
    if(cnt < 8):
        tmp += cnt * int(i)
        cnt *= 2
    else:
        ans += str(tmp)
        tmp = 1 * int(i)
        cnt = 2
ans += str(tmp)
print(int(ans[::-1])) 
