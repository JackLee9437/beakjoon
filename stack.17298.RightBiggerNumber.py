from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
A = tuple(map(int,input().split()))

ans = [0] * N
stk = deque()

for i in range(N-1,-1,-1) :
    while stk and stk[-1] <= A[i] :
        stk.pop()

    if not stk :
        ans[i] = -1
    else :
        ans[i] = stk[-1]
    stk.append(A[i])
    
print(' '.join(map(str,ans)))



'''
π€π€π€ λ¬Έμ μ μλ₯Ό μ νμ π€π€π€

μλ ₯ : 
μΆλ ₯ : 

μ°ΎμμΌνλ κ° : 
μκ³ λ¦¬μ¦ : 

-----



-----


'''