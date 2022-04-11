from sys import stdin
input = stdin.readline

class Queue :
    def __init__(self, capacity) :
        self.capacity = capacity
        self.que = [0] * capacity
        self.cnt = 0
        self.frt = 0
        self.rear = 0

    def push(self,val) :
        if self.cnt < self.capacity :
            self.que[self.rear] = val
            self.cnt += 1
            self.rear += 1
            if self.rear >= self.capacity : self.rear = 0

    def pop(self) :
        if self.cnt > 0 :
            temp = self.que[self.frt]
            self.frt += 1
            self.cnt -= 1
            if self.frt >= self.capacity : self.frt = 0
            return temp

    # def size(self) :
    #     print(self.cnt)

    # def empty(self) :
    #     print(0 if self.cnt else 1)

    # def front(self) :
    #     print(self.que[self.frt] if self.cnt else -1)

    # def back(self) :
    #     print(self.que[self.rear-1] if self.cnt else -1)


N = int(input())
que = Queue(N)
for n in range(1,N+1) :
    que.push(n)

while que.cnt > 1 :
    que.pop()

print(que.pop())






'''
🤔 문제정의를 잘 하자 🤔

입력 : 
출력 : 

찾아야하는 값 : 
알고리즘 : 

-----


-----

'''