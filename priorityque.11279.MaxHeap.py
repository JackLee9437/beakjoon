import heapq as hq
from sys import stdin
input = stdin.readline

N = int(input())
maxHeap = []

for _ in range(N) :
    cmd = int(input())
    
    if cmd == 0 :
        if len(maxHeap) == 0 :
            print(0)
        else :
            print(-hq.heappop(maxHeap))
    else :
        hq.heappush(maxHeap, -cmd)
    

    


'''
π€ λ¬Έμ μ μλ₯Ό μ νμ π€

μλ ₯ : μ°μ°μ κ°μ N, μ°μ°μ λν μ λ³΄λ₯Ό λνλ΄λ μ μ x
μΆλ ₯ : 0μ΄ μ£Όμ΄μ§ νμλ§νΌ λ΅ μΆλ ₯. λ°°μ΄μ΄ λΉμ΄μλ κ²½μ°μλ 0 μΆλ ₯

μ°ΎμμΌνλ κ° : 
μκ³ λ¦¬μ¦ : 

-----


-----

'''