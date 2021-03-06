import heapq as hq
from sys import maxsize, stdin, setrecursionlimit
input = stdin.readline

setrecursionlimit(1000000)

N = int(input())
cards = [int(input()) for _ in range(N)]

hq.heapify(cards)

def compCards(arr) :
    if len(arr) == 1:
        return 0
    else:
        min1 = hq.heappop(arr)
        min2 = hq.heappop(arr)
        temp = min1+min2
        if not arr :
            return temp
        hq.heappush(arr, temp)
        return temp + compCards(arr)

print(compCards(cards))




'''
๐ค ๋ฌธ์ ์ ์๋ฅผ ์ ํ์ ๐ค

์๋ ฅ : ์ซ์์นด๋ ๋ฌถ์ ์ N, ๊ฐ ๋ฌถ์๋ณ ์นด๋ ์ minHeap
์ถ๋ ฅ : ํ์ํ ์ต์ ๋น๊ต ํ์

์ฐพ์์ผํ๋ ๊ฐ : 
์๊ณ ๋ฆฌ์ฆ : ์ฐ์ ์์ ํ

-----
์ฌ๊ท ๋์๊ฐ ๋ฌผ์ฌ ๋จ. ๋ฐ๋ณต๋ฌธ๋ ๊ฐ๋ฅํ ๋ฏ.
N๊ฐ ์นด๋ ์ค์ ํญ์ ์ต์ 2๊ฐ๋ง ๊ฐ์ง๊ณ  ํฉ์ ๊ตฌํด์ค์ผํจ.
- ๋๊ฐ๋ฅผ ํฉ์น๋ฉด ๊ทธ ํฉ์น๊ฒ ์์ด์ผํ๋ ๋ฌถ์ ์ค์ ๋ ํ ๋ฌถ์์ด ๋๊ธฐ ๋๋ฌธ์ ๋ค์ ๋น๊ต์ ๋์์ด ๋๋ค๋ ์๋ฏธ.
- ์ฆ ์ผ๋จ ๋ค ์ต์ํ์ ๋ค ๋ฃ๊ณ , ์์๋๋ก ๋๊ฐ ๋นผ์ ๋ํจ. ๊ทธ ๋ํ๊ฑด ๋น๊ต ํ์๊ฐ ๋๊ธฐ๋๋ฌธ์ ์ผ๋จ sum์ ์ ์ฅ
- ๊ทธ๋ฆฌ๊ณ  ๋ค์ ๊ทธ ํฉ์น๊ฑฐ๊ฐ ๋น๊ต๋์์ด ๋๋๋ก ํ์ ๋ฃ์. ๊ทธ๋ฌ๊ณ  ๊ทธ ๊ณผ์ ์ ๋ฐ๋ณต!


-----


'''