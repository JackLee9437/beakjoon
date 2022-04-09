from sys import stdin
input = stdin.readline

class Stack :
    def __init__(self, capacity) :
        self.stk = [0] * capacity
        self.ptr = 0
    
    def push(self, val) :
        self.stk[self.ptr] = val
        self.ptr += 1

    def pop(self, val=1) :
        if self.ptr > 0 :
            self.ptr -= val

    def empty(self) :
        return True if self.ptr<=0 else False


N, K = map(int,input().split())
num = input().strip()







'''
🤔 문제정의를 잘 하자 🤔

입력 : 자리수 N, 뺄개수 K, 숫자 num
출력 : 얻을 수 있는 가장 큰 수

찾아야하는 값 : 얻을 수 있는 수 중의 가장 큰 수
알고리즘 : 완전탐색? 이분탐색? 스택?

-----
완전탐색?
- 자리수 N에서 K를 빼면 결과로 얻을 수 있는 숫자의 자리수를 알 수 있으므로, num에서 그 자리수만큼 combination을 구한다음 원 순서에 맞게 재구성하고 최대값을 구하는 방법 - 원래 위치대로 바꿔줘야하고 모든 경우의 수를 따지면 너무 오래걸림
- 동일한 방법으로 필요한 자리수부터 구하고, 글자에서 처음부터 가면서 가장 큰거, 그 다음 큰거, 그다음 큰거 구하는 방법
    - 주의해야할 점 : 숫자의 순서가 바뀌면 안됨!


-----

'''