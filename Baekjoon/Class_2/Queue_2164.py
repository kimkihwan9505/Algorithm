from collections import deque
n = deque()
a =int(input())
for i in range(a):
    n.append(i+1)
    
while len(n) >1:
    n.popleft()
    n.append(n.popleft())
print(n[0])

'''
a = int(input())
num=[]
for i in range(1,a+1):
    num.append(i)
    
for _ in range(len(num)):
    if len(num) > 1:
        num.pop(0)
        num.append(num.pop(0))
    elif len(num) ==1:
        print(num[0])
        
일반 리스트로 하면 시간초과
'''
