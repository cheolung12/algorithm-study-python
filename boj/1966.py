import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    queue = list(map(int,input().split()))
    cnt = 0

    while(M != -1):     # m이 -1이면 큐를 빠져나온것
        if queue[0] == max(queue):
            del queue[0]
            M -= 1
            cnt += 1
        else:
            queue.append(queue[0])
            del queue[0]        # 뒤로만 보내고 인쇄하는건 아니니까 cnt는 그대로

            if M==0:
                M = len(queue) - 1  # 인덱스 값도 맨 뒤로 조정
            else:
                M -= 1    
    print(cnt)       