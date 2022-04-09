from sys import stdin, maxsize
input = stdin.readline

M, N, L = map(int,input().split())
X = tuple(sorted(map(int,input().split())))
A = tuple(tuple(map(int,input().split())) for _ in range(N))

cnt = 0

for a, b in A :
    if b > L : # 여기도 애초에 L보다 크면 제외해주는 부분인데 괜히 시간 늘어남 ㅠ.. x개 빼겠다고 n번 연산이 더들어가는게 문제인가.. 그렇다고 하기엔 밑에 연산이 더 많은데 ㅠ
        continue
    Lprime = L - b
    aL = a - Lprime
    aR = a + Lprime

    pL = 0
    pR = M-1

    # if X[0] >= aL and X[-1] <= aR : 애초에 X가 범위안에 있으면 카운트 해주려고 했으나, 그런 경우가 별로 없는듯. 시간만 더걸림 ㅠ
        # cnt += 1
    # else :
    while pL <= pR :
        pM = (pL + pR) // 2
        if aL <= X[pM] <= aR :
            cnt += 1
            break
        if X[pM] < aL :
            pL = pM + 1
        elif aR < X[pM] :
            pR = pM - 1
    

print(cnt)



'''
🤔 문제정의를 잘 하자 🤔

입력 : 사대의 수 M, 동물의 수 N, 사정거리 L, /n, 사대 위치 X, 동물 위치 A
출력 : 잡을 수 있는 동물의 수 ans

찾아야하는 값 : X의 각 원소로부터 사정거리 L 안에있는 동물 A의 수
알고리즘 : 이분탐색

-----
완전탐색의 경우
- 사대기준 : A의 위치까지의 거리를 구해서 L 안에 있는 경우 카운트를 올릴 수 있겠으나, 사대마다 A를 중복으로 찾게되어 이를 막기 위한 비트마스크 필요해보임. 좋지 않을듯
- 동물기준 : 사대 위치까지 한번이라도 L 안에 있으면 카운트 1 올리기. 찾는 방법은 Ai 마다 for문으로 abs(Xi-ai) - bi 구해서 L 보다 작으면 카운트 추가 및 for문 종료,,
- 사정거리 기준 : 동물기준으로 먼저 사정거리를 2차원적으로 (x축방향으로) 만들고, X 있는 사대중에 사정거리 L' 안에서 하나라도 발견되면 끝.

이분탐색의 경우
- 동물/사정거리 기준 : 동물은 all scan해야할듯. 동물기준 사정거리를 2차원 길이 L'로 만들고, x의 최소, 최대 가능만 찾기. X의 첫번째와 마지막 원소만 비교해서 X[0] 이 xl보다 작고 X[-1]이 xr보다 크기만 하면 무조건 잡힘.
- 좀더 개선? : 위 대로만 하면, 그 사이에 없는 경우가 더 많아서 카운팅이 안됨. 오히려 만번중 한번이라 계산횟수만 늘려서 느려질 수 있음. 방법은, 이분탐색으로 X 원소 탐색해서 L' 범위 안에 있는지 찾아보는 방법.
-----

'''