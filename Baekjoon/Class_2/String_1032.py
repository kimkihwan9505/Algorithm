
a = int(input())
b= list(input())
for _ in range(a-1):
    c=list(input())    
    for i in range(len(b)):
        if b[i] != c[i]:
            b[i]="?"
print(''.join(b))            
