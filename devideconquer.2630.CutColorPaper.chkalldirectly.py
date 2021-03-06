from sys import stdin
input = stdin.readline

N = int(input())
paper = tuple(tuple(map(int,input().split())) for _ in range(N))

whiteCnt = 0
blueCnt = 0

def cut_paper(arr, n, p : tuple = (0, 0)) :
    global whiteCnt, blueCnt
    color = arr[p[0]][p[1]]
    isBraked = False
    for i in range(p[0],p[0]+n) :
        for j in range(p[1],p[1]+n) :
            if arr[i][j] != color :
                isBraked = True
                break
        else : continue
        break
    else :
        if color == 1 :
            blueCnt += 1
        else :
            whiteCnt += 1
    if isBraked :
        cut_paper(arr, n//2, (p[0],p[1]))
        cut_paper(arr, n//2, (p[0],p[1]+n//2))
        cut_paper(arr, n//2, (p[0]+n//2,p[1]))
        cut_paper(arr, n//2, (p[0]+n//2,p[1]+n//2))

cut_paper(paper, N)
print(whiteCnt)
print(blueCnt)


'''
๐ค ๋ฌธ์ ์ ์๋ฅผ ์ ํ์ ๐ค

์๋ ฅ : ์ ์ฒด ์ข์ด ํ๋ณ์ ๊ธธ์ด N, ์์ข์ด์ ์ ์ฌ๊ฐํ ์๋ค ์ ๋ณด (NbyN) (ํฐ์ 0 ํ๋์ 1)
์ถ๋ ฅ : ํ์์ ์ข์ด ๊ฐ์ whiteCnt \n ํ๋์ ์ข์ด ๊ฐ์ blueCnt

์ฐพ์์ผํ๋ ๊ฐ : ํฐ/ํ๋ ์ ์ข์ด ๊ฐ์
์๊ณ ๋ฆฌ์ฆ : ๋ถํ ์ ๋ณต๋ฒ,,, -> ์ฌ๊ท? ๋๋ ๋ฐ๋ณต๋ฌธ?

-----
N์ด 1์ด ๋ ๋๊น์ง ์ฌ๊ท์ ์ผ๋ก ๋ค์ด๊ฐ์ all๋ก ๋ค 1์ด๊ฑฐ๋ ๋ค 0์ธ์ง ์ฐพ๊ณ  ์๋๋ฉด ๋ค์ ์ฐข์ด์ ์ฌ๊ท๋ก ๋ค์ด๊ฐ๊ณ , ๋ง์ผ๋ฉด cnt ์ฌ๋ฆฌ๋๋ก.

์ด๋ง๋ค ๋ค์ด๊ฐ๋ฉด์ ํ์ธ ํ์.
all ์ด True์ฌ์ ์ ๋ถ 1์ด๋ฉด whiteCnt + 1
any๋ก True ๋์ค๋ฉด 1์์ธ๊ฑฐ๋๊น ๋ถํ 
any๊ฐ False ๋์ค๋ฉด 0๋ง ์์ผ๋๊น blueCnt + 1

์ฌ๊ท ๋๋ฆด๋ arr, N, ์ฌ๋ถ๋ฉด๋ง ์ ๋ฌ์์ ์ฌ๊ทํธ์ถํด์ ๋ค์๋จ๊ณ ์งํ์ ๋ฐฐ์ด์ ์ด๋์๋ถํฐ ๋์ด์ผํ ์ง๊ฐ ์ด๋ ค์. ์ถ๊ฐ ์ธ์ ์ ๋ฌ ํ์.
์ฌ๋ถ๋ฉด์ ๋ฐ๋ผ ์ค์  ์์น (ํ๋๋ง) ์ ๋ฌํด์ฃผ๊ธฐ.

-----

'''