while True:
    try:
        sentense = input()
        result = [0] * 4
        for a in sentense:
            if('a' <= a <= 'z'):
                result[0] += 1
            elif('A' <= a <= 'Z'):
                result[1] += 1
            elif(a.isdigit() == True):
                result[2] += 1
            elif(a == " "):
                result[3] += 1 
        print(*result)
    except EOFError:
        break
