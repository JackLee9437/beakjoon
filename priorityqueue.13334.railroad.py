import heapq as hq
from sys import stdin
input = stdin.readline

n = int(input())
people = [sorted(list(map(int,input().split()))) for _ in range(n)]
d = int(input())

people.sort(key= lambda x:x[1])
heap = []
rst = 0

for start, end in people :
    lim = end - d
    if start >= lim :
        hq.heappush(heap, start)
    while heap and heap[0] < lim :
        hq.heappop(heap)
    rst = max(rst,len(heap))

print(rst)









'''
🤔 문제정의를 잘 하자 🤔

입력 : 사람의 수 n, 사람들의 집/오피스 좌표 (hi,oi) 리스트 people, 철로의 길이 d
출력 : 집과 사무실 위치가 모두 선분에 포함되는 사람들의 최대 수

찾아야하는 값 : 
알고리즘 : 우선순위 큐, 정렬?, 스위핑? - 나와있는건 잘 살피기... ㅠ

-----
초기 생각이 근접했으나 좀 더 정확하지 못했음... heap에 구간 내 가능한 사람들을 저장해주는건 good... 하지만 입력받은애를 힙으로 할 필욘 없음.. 

시작점부터 확인하니까 안들어오는 애들을 버리기가 어려움
-> 마지막 점으로 확인해야할듯함... 어떻게?
people은 힙으로 두지 말고 정렬된 list로 만들기
heap 은 해당 구간 내 들어오는 애들만 넣기 -> 마지막시점 기준 멈추면서 스캔 - 시작위치 들어오는애들 힙에 추가 // 이전에 추가했지만 시작위치 들어오지 않는애들은 pop -> 힙에 있는 갯수로 확인 가능~

hi,oi 가 오름차순이 아닐 수 있기 때문에 오름차순으로 정렬 받아야 함!

-----


'''