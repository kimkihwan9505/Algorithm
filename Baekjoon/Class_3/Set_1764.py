import sys
input = sys.stdin.readline

a,b =map(int,input().split())

A=set()
for _ in range(a):
    A.add(input().rstrip())
    
B=set()
for _ in range(b):
    B.add(input().rstrip())
    
tmp=sorted(list(A & B))

print(len(tmp))
for i in tmp:
    print(i)
