from collections import deque
from sys import stdin
input = stdin.readline

perens = input().strip()
stk = deque()

sticks = -1
pieces = 0

for idx, peren in enumerate(perens) :
    if peren == "(" :
        stk.append(peren)
        sticks += 1
        continue

    if perens[idx-1] == "(" :
        pieces += sticks
    else :
        pieces += 1
    sticks -= 1
    stk.pop()
    
print(pieces)



'''
π€π€π€ λ¬Έμ μ μλ₯Ό μ νμ π€π€π€

μλ ₯ : 
μΆλ ₯ : 

μ°ΎμμΌνλ κ° : 
μκ³ λ¦¬μ¦ : 

-----



-----


'''