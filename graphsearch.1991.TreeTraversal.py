from sys import stdin
input = stdin.readline



N = int(input())
tree = {}
for _ in range(N) :
    root, left, right = input().rstrip().split()
    tree[root] = (left,right)

def preorder(root) :
    if root != "." : 
        print(root, end="")
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root) :
    if root != "." : 
        inorder(tree[root][0])
        print(root, end="")
        inorder(tree[root][1])

def postorder(root) :
    if root != "." : 
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end="")

preorder("A")
print()
inorder("A")
print()
postorder("A")


'''
π€π€π€ λ¬Έμ μ μλ₯Ό μ νμ π€π€π€

μλ ₯ : 
μΆλ ₯ : 

μ°ΎμμΌνλ κ° : 
μκ³ λ¦¬μ¦ : 

-----



-----


'''