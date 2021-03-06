from collections import deque
from sys import maxsize, stdin
input = stdin.readline

N = int(input())
circles = [tuple(map(int,input().split())) for _ in range(N)]

lr_circles = []
for circle in circles :
    l = circle[0] - circle[1]
    r = circle[0] + circle[1]
    lr_circles.append((l,r))
lr_circles.sort(reverse=True, key= lambda x: x[1])
lr_circles.sort(key= lambda x: x[0])
# print(lr_circles)

stk = deque()
contacts = set()

e = 0

for circle in lr_circles :
    if not stk :
        stk.append(circle)
        print(circle, stk, e, contacts)
        continue

    if stk[-1][0] == circle[0] :
        contacts.add(circle[0])
        stk.append(circle)
    elif stk[-1][0] < circle[0] < stk[-1][1] :
        stk.append(circle)
    elif circle[1] == stk[-1][1] :
        contacts.add(circle[1])
        stk.append(circle)
    else :
        if stk[-1][1] == circle[0] :
            contacts.add(circle[0])
        while stk and stk[-1][1] <= circle[0] :
            temp = stk.pop()
            if stk and temp[1] == stk[-1][1] :
                contacts.add(temp[1])
            if temp[0] in contacts and temp[1] in contacts :
                e += 2
            else :
                e += 1
        stk.append(circle)
    print(circle, stk, e, contacts)

while stk :
    temp = stk.pop()
    if stk and temp[0] < stk[-1][1] :
        if temp[1] == stk[-1][1] :
            contacts.add(temp[1])
        if temp[0] in contacts and temp[1] in contacts :
            e += 2
        else :
            e += 1
    else : 
        if temp[0] in contacts and temp[1] in contacts :
            e += 2
        else :
            e += 1

    
print(temp, stk, e, contacts)

v = len(contacts)
f = 2-v+e
# print(v,e,f)
print(f)



'''
π€π€π€ λ¬Έμ μ μλ₯Ό μ νμ π€π€π€

μλ ₯ : μμ κ°μ N, μμ μ λ³΄ x,r
μΆλ ₯ : μμΌλ‘ μΈν΄ λ§λ€μ΄μ§λ μμ­μ μ

μ°ΎμμΌνλ κ° : μ€μΌλ¬μ§ν v-e+f=1 μ λ°λΌ, f=1-v+e. ans = f + 1. μ¦, κΌ­μ§μ‘κ³Ό λ³μ μλ§ κ΅¬νλ©΄ λ¨. 
μκ³ λ¦¬μ¦ : μ λ ¬(μΌλ¨ μΌμͺ½λΆν° νμΈνλ €λ©΄ μ λ ¬ νμνλ―), μλ£κ΅¬μ‘°, μ€ν(μ€νμ μ΄λ»κ² μ¨λ¨ΉμκΉ...), μ€μΌλ¬μ§ν

-----
μ νλ μμ΄ μκ±°λ μμ΄ νλλ§ μ νλ©΄ μΌλ¨ μ μ μ νκ°.
μμ΄ μμͺ½μΌλ‘ μ νλ©΄ μ μ΄ λκ°.

μ νκ°λΉ λ³μ 1κ° λλ λκ°. μ μ μ΄ 1κ°λ©΄ 1κ°, 2κ°λ©΄ λκ°.

μ€μΊνλ©΄μ νμΈν΄μΌν  λ΄μ©
- μμ μΌ/μ€ μ’ν
- νλμ μμ λν΄ μ νλ μμ΄ μλμ§, λͺκ°μλμ§


μ€ν¨μμΈ
1. μκ°μ΄κ³Ό
2. μ€μΌλ¬μ§νκ°... μ...

λ°λ‘ :
5
2 2
1 1
3 1
8 3
12 1

μ€μΌλ¬μ§νλ₯Ό μ νν μ΄ν΄νμ§ λͺ»ν λΆλΆ,,
https://velog.io/@phw1996/Python-%EB%B0%B1%EC%A4%80-10000%EB%B2%88-%EC%9B%90-%EC%98%81%EC%97%AD-%ED%92%80%EC%9D%B4

μ€μΌλ¬μ§νλ₯Ό μ¬μ©ν΄μ λ¬Έμ  νλ €λ©΄ v,eλ μμΈμ μΌλ‘ λ€λ₯΄κ² μκ°ν΄μ£Όμ΄μΌνκ³ ,
v-e+f=2λ‘ μμκ° κ³ μ μ μΈκ² μλλΌ μ»΄ν¬λνΈ c κ°μ κ΅¬ν΄μΌνλ―λ‘ μ λμ¨ νμΈλ μκ³ λ¦¬μ¦ μ΄λκ±Έ μ μ©ν΄μΌν¨.
λμ€μ μΆκ°λ‘ κ³΅λΆνκΈ°λ‘ νκ³  μ΄λ²μ ν¨μ€...
-----


'''