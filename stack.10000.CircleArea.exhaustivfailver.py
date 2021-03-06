from sys import maxsize, stdin
input = stdin.readline

def isContact(presC,compC) :
    xDiff = presC[0] - compC[0]
    if xDiff == presC[1] + compC[1]  : 
        return ("lo", presC[0] - presC[1])
    elif xDiff == presC[1] - compC[1] : 
        return ("li", presC[0] - presC[1])
    elif -xDiff == presC[1] + compC[1]  :
        return ("ro", presC[0] + presC[1])
    elif -xDiff == presC[1] - compC[1] :
        return ("ri", presC[0] + presC[1])
    return False

N = int(input())
circles = [tuple(map(int,input().split())) for _ in range(N)]

lineCntLeft = [0] * N
lineCntRight = [0] * N
contacts = set()

circles.sort()

for i in range(N-1) :
    for j in range(i+1,N) :
        if lineCntLeft[i] and lineCntRight[i] :
            break
        temp = isContact(circles[i],circles[j])
        # print(i,j,temp)
        if temp and temp[0][0] == "l" :
            if temp[0][1] == "i" :
                lineCntLeft[i] = lineCntLeft[j] = 1
            elif temp[0][1] == "o" :
                lineCntLeft[i] = lineCntRight[j] = 1
            contacts.add(temp[1])
        elif temp and temp[0][0] == "r" :
            if temp[0][1] == "i" :
                lineCntRight[i] = lineCntRight[j] = 1
            if temp[0][1] == "o" :
                lineCntRight[i] = lineCntLeft[j] = 1
            contacts.add(temp[1])
        
        
v = len(contacts)
e = 0
for k in range(N) :
    if lineCntLeft[k] and lineCntRight[k] :
        e += 2
    else : e += 1
f = 2-v+e
# print(lineCntLeft)
# print(lineCntRight)
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