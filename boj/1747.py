N = int(input())

# 에라토스테네스의 체
def asieve(N):
    sieve = [False, False] + ([True] * (N-1))
    limit = int(N ** 0.5)
    for i in range(2, limit+1):
        if sieve[i] :
            for j in range(i*2, N+1, i):
                sieve[j] = False
    return [i for i in range(2, N+1) if sieve[i]]

# 팰린드롬
def pellin(li):
    result = []
    for i in li:
        if int(str(i)[::-1]) == i:
            result.append(i)
    return result

selection = asieve(1000000)
selection = pellin(selection)

res = 0
for i in selection:
    if i >= N:
        res = i
        break

if res == 0:
    res = 1003001
print(res)        