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


N = int(input())
towers = tuple(map(int,input().split()))
towRcv = [0] * N

# stk = Stack(N)

for i in range(N-1,0,-1) :
    temp = 0
    for j in range(i-1,-1,-1) :
        if towers[i] < towers[j] :
            temp = j+1
            break
    towRcv[i] = str(temp)
towRcv[0] = '0'

print(' '.join(towRcv))





'''
🤔 문제정의를 잘 하자 🤔

입력 : 탑들의 개수 N, 탑들의 순서 및 크기 towers 
출력 : 각각의 탑에서 발사한 레이저 신호를 어느 탑에서 수신하는지 알아내야함.

찾아야하는 값 : 탑마다 수신하는 탑의 위치. 없으면 0
알고리즘 : 완전탐색? 이분탐색? 근데 원주제는 스택?

-----
완전탐색으로?
- 왼쪽부터 가면서, 0번째 인덱스는 당연히 0. 수신가능한 탑을 L, 송신하는 탑을 R이라고 하면, L보다 높은 R을 발견할 때마다 L 갱신 및 R은 0. L보다 낮은 R을 발견하면 R을 수신하는애는 L이 됨
    - N이 작을때는 쉽지만, 주어진 문제대로 500000 같이 많으면 찾는데 한참 걸림
    - 문제점! L이 갱신된 후에 작은 R을 만났을 경우, 그 다음에는 기존 R보다 크냐 작냐에 따라 L이 수신할 수도 R이 수신할 수도 있어 분기 필요해보임. 심지어 다음 발견된게 또 L보다 작게되면 그 다음에 비교할 대상이 많아져버림
- 오른쪽에서 오면서, R보다 큰 값을 만날때마다 값 등록. 큰 값이 없으면 0. 끝은 그냥 0. 가능함,, 하지만 이것도 N이 클때는 시간초과임

이분탐색으로 가능?
- 처음으로 큰 값을 만나는 것이 답이 되어야 하는데, 순서가 중요해서 정렬을 할 수 없다보니 어느것이 처음으로 만나는 큰 탑인지 범위를 정하기 어려움


스택으로?
- 기둥세우기 문제의 경우랑 비슷한 면이 있음. 오른쪽애를 R로 두고, 하나씩 꺼내다가 더 큰거 발견하면 cnt 올리고 R을 갱신했었음.
- 완전탐색이랑 같은 방법으로 풀되, 스택만 사용해서 가능할 듯 함. 하지만 사이즈가 클때 시간초과됨,,,
    - 핵심은, N개를 전부 찾아야되는건 아닐 듯 함!!!
-----

'''