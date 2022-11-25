n,m = map(int,input().split())

# 에라토스테네스의 체 초기화 : n개 요소에 True 설정 (소수로 간주)
sieve = [False, False] + [True] * (m-1)
limit = int(m ** 0.5)

for i in range(2, limit+1):
    if sieve[i] == True: # i 가 소수인 경우
        for j in range(2*i, m+1, i): # i 이후 i의 배수는 False로 판정한다.
            sieve[j] = False
# 만들어진 소수 목록 산출 
primes = [i for i in range(2,m+1) if sieve[i]== True]

for prime in primes:
    if prime >= n:
        print(prime)