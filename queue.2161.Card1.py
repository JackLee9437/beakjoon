from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())

cards = deque()
for i in range(1,N+1):
    cards.append(i)
    
ans = ""

while cards :
    ans += str(cards.popleft()) + " "
    cards.rotate(-1)
print(ans)




'''
π€π€π€ λ¬Έμ μ μλ₯Ό μ νμ π€π€π€

μλ ₯ : 
μΆλ ₯ : 

μ°ΎμμΌνλ κ° : 
μκ³ λ¦¬μ¦ : 

-----



-----


'''