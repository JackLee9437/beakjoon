from sys import stdin, setrecursionlimit
input = stdin.readline

setrecursionlimit(10**6)

preorder = []
while True :
    try :
        preorder.append(int(input()))
    except :
        break

def postorder(left, right) :
    # print(left,right)
    if left > right : return
    else :
        idx = right + 1
        for i in range(left+1,right+1) :
            if preorder[left] < preorder[i] :
                idx = i
                break
        postorder(left+1,idx-1)
        postorder(idx,right)
        print(preorder[left])
            
postorder(0,len(preorder)-1)

'''
π€π€π€ λ¬Έμ μ μλ₯Ό μ νμ π€π€π€

μλ ₯ : 
μΆλ ₯ : 

μ°ΎμμΌνλ κ° : 
μκ³ λ¦¬μ¦ : 

-----



-----


'''