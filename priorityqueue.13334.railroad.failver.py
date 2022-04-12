import heapq as hq
from sys import stdin
input = stdin.readline

n = int(input())
people = [tuple(map(int,input().split())) for _ in range(n)]
d = int(input())

hq.heapify(people)
tempHeap = []

line = [people[0][0],people[0][0]+d] # 현재 스캔하는 위치
max = 0
cnt = 0


while people :
    while people :
        temp = hq.heappop(people)
        if temp[0] >= line[0] and temp[1] <= line[1] :
            cnt += 1
            if temp[0] != line[0] :
                hq.heappush(tempHeap,temp)
        elif temp[0] > line[0] :
            hq.heappush(people,temp)
        
        if temp[0] > line[1] :
            if cnt > max : 
                max = cnt
                break
            
    else : break
    if tempHeap : 
        line = [tempHeap[0][0], tempHeap[0][0] + d]
        cnt = len(tempHeap)
        while tempHeap[0][0] == line[0] :
            hq.heappop(tempHeap)
            if not tempHeap : break
    else :
        line = [people[0][0], people[0][0] + d]
        cnt = 0
    # print(people)

print(max)
        







'''
🤔 문제정의를 잘 하자 🤔

입력 : 사람의 수 n, 사람들의 집/오피스 좌표 (hi,oi) 리스트 people, 철로의 길이 d
출력 : 집과 사무실 위치가 모두 선분에 포함되는 사람들의 최대 수

찾아야하는 값 : 
알고리즘 : 우선순위 큐, 정렬?, 스위핑?

-----
최대 수 를 구한다고 했지만, 최대수를 계속 최대힙에 갱신하면서 최대값을 찾는다? 그건 의미가 없음. 
왜냐면 우선순위 큐라는건 뭔가 구하는 과정인데 그게 아니라 결과를 만들고 있는데서 효율이 떨어지기도 하고 그냥 최대값 변수로도 충분히 갱신이 가능함. -> max 저장 변수 사용

그림을 봤을 땐 왼쪽부터 오른쪽으로 이동하면서 스캔해줄 필요가 있어보임. - 이게 스위핑인가?
여기서 hi 의 작은 위치부터 확인할 필요가 있음. -> sort로도 가능할거같긴 함. 오름차순 정렬 후 pop(0) 해주면 첫번째 아이템부터 나오긴 할테니... 그래서 정렬이 포함되어있나?
처음부터 힙푸쉬로 넣을 필요는 없음. 어차피 다 넣어놓고 하나씩 뺄꺼니까,, 입력받고 heap 방식으로 바꾸면 될듯.

L을 좌표로 만들어서 끝까지 스캔.
- 힙을 한개 쓴다?
죄다 한개에 몰아놓고, 최소꺼 빼서 거기부터 그다음 위치, 그다음 위치로 가면서 스캔. 스캔할때마다 개수 세서 max 갱신. 
시작점이 같은 애들은 pop해서 버리고, 다른애들은 temp에 저장했다가 다시 push. 다음 확인할때 사용. 꺼냈을때 위치만 저장해두기. => 팝했다가 다시 푸쉬하면 무슨소용이람 ㅠ
- 힙을 두개 쓴다?
같은 방법이지만 현재 구간에 있는 애들을 보관하기 위해 힙 하나 더쓰는 방법?
시작점이 겹치면 스캔해서 확인하고 구간 내 있는 다른 점들은 힙에 저장, 그다음 시작점 지나면 팝. 그러면 힙에 저장되어있는 개수로 max 확인 가능.
하지만 push, pop 이 늘어서 시간에 안좋지 않을까,, => 일단 해보자. 확인했는데 구간 안에 남아있는 애들은 새로운 힙큐에 넣어주기.

실패.... ..ㅓㄹ햐ㅐㅓㄹ댜ㅐㅁㅈ럳먀재ㅓㄹ먀ㅐ저랴ㅐㅁㅈ렂먀ㅐㄷ러ㅑㅐ럼쟈ㅐㄹㄷㅈ머랴
하나라도 구간내에 안들어오면, 그 다음꺼가 구간 내에 들어오는지 확인하기가 어려워짐 (안들어온애는 다음에 확인해야하는데 보관해둘데가 없음...)

시작점부터 확인하니까 안들어오는 애들을 버리기가 어려움
-> 마지막 점으로 확인해야할듯함... 어떻게?
people은 힙으로 두지 말고 정렬된 list로 만들기
heap 은 해당 구간 내 들어오는 애들만 넣기 -> 마지막시점 기준 멈추면서 스캔 - 시작위치 들어오는애들 힙에 추가 // 이전에 추가했지만 시작위치 들어오지 않는애들은 pop -> 힙에 있는 갯수로 확인 가능~


-----


'''