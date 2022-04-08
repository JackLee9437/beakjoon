from sys import stdin
input = stdin.readline

N, C = map(int,input().split())
x = tuple(sorted([int(input()) for _ in range(N)]))

left = 1
right = (x[-1]-x[0]) // (C-1) + 1

ans = 0

while left <= right :
    tempLen = (left + right) // 2
    
    curntP = x[0]
    cnt = 1
    
    for i in range(1, N) :
        if x[i] - curntP >= tempLen :
            cnt += 1
            curntP = x[i]
    
    if cnt >= C :
        ans = tempLen
        left = tempLen + 1
    else :
        right = tempLen - 1
    
print(ans)


'''
입력 : 
출력 :

찾아야하는 값 (이분탐색 하려고 하는 결과값) : 

산성 양의 정수
알칼리 음의 정수

특성값이 0에 가까운 용액 만들기


'''