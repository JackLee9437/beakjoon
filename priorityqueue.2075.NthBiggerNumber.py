import heapq as hq
from sys import stdin
input = stdin.readline

N = int(input())
minHeap = []

for _ in range(N) :
    arr = tuple(map(int,input().split()))

    if not minHeap :
        for num in arr :
            hq.heappush(minHeap,num)
    else :
        for num in arr :
            if num > minHeap[0] :
                hq.heappush(minHeap,num)
                hq.heappop(minHeap)
print(minHeap[0])
            


'''
π€π€π€ λ¬Έμ μ μλ₯Ό μ νμ π€π€π€

μλ ₯ : 
μΆλ ₯ : 

μ°ΎμμΌνλ κ° : 
μκ³ λ¦¬μ¦ : 

-----



-----


'''