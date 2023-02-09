import sys
 
data = sys.stdin.readline().rstrip()

for alpa in data:
    if(alpa.isupper() is True):
        temp = ord(alpa) + 13
        if(temp > 90):
            temp -= 26
        print(chr(temp),end='')
    elif(alpa.islower() is True):
        temp = ord(alpa) + 13
        if(temp > 122):
            temp -= 26
        print(chr(temp),end='')
    else:
        print(alpa,end='')