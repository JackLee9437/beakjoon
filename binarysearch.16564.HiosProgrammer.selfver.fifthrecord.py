from sys import stdin, maxsize
input = stdin.readline

N, K = map(int,input().split())
X = tuple(sorted([int(input()) for _ in range(N)]))

pL , pR = 0, N - 1
fullIdx = 0
temp = 0

while pL <= pR :
    pM = (pL + pR) // 2
    
    if X[pM] - X[0] > K :
        pR = pM - 1
        continue
    compTemp = X[pM]*(pM) - sum(X[:pM])
    if compTemp <= K :
        fullIdx = pM
        temp = compTemp
        pL = pM + 1
    else : 
        pR = pM - 1

remainK = K - temp

ableK = remainK // (fullIdx + 1)
T = X[fullIdx] + ableK
print(T)




'''
🤔 문제정의를 잘 하자 🤔

입력 : 캐릭터의 개수 N, 올릴 수 있는 레벨 총합 K, 캐릭터 레벨 list X
출력 : 가능한 최대 팀 목표레벨 T

찾아야하는 값 : K를 분배해서 레벨업 한 다음에 만들 수 있는 캐릭터list 중 최소값이 최대가 될 때의 값
알고리즘 : 이분탐색 (완전탐색으로 가능)

-----
완전탐색으로 푼다면
- K를 크기가 N개인 배열에 나눠담는 경우의 수를 구하고 돌아가면서 X에 더하면서 최소값을 구하면서 그중에 최대값으로 갱신하는 방법
- X를 오름차순 정렬 한 다음 0번째 원소에 1번째 원소만큼 채움. 그리고 0과 1번째 원소에 2번의 원소만큼 채울 수 있는만큼 채움 ....
-> 수가 많아지면 느릴듯

이분탐색으로 한다면?
- 캐릭터 리스트의 중간에서 나머지 값들과의 차이 비교해서 K 를 채울 수 있을지 판단. K보다 크면 R을 중간보다 왼쪽으로, K보다 작으면 L을 중간보다 오른쪽으로
- 수가 너무 크면 for 문 돌려서 차이 비교하는것도 오래걸릴 것 같음. -> 첫번째 원소와 중간 원소를 먼저 비교해서 K보다 크면 R을 왼쪽으로
- 종료시점은? L과 R의 교차
- 결과값은? 해당 위치에서 일단 꽉 채워져있음. K에서 채워진만큼 뺀다음, 동등하게 나눠서 분배(//) 하고 더해주면 답.


-----

'''