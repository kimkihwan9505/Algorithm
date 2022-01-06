n,m=map(int,input().split())        
board=[]
result=[]
for _ in range(n):
    board.append(input())
    
for i in range(n-7):
    for j in range(m-7):
        b,w=0,0
        for k in range(i,i+8):
            for h in range(j,j+8):
                if (k+h)%2==0: #짝수 시작
                    if board[k][h] !='B':
                        b+=1
                    if board[k][h] !='W':
                        w+=1
                else : # 홀수 시작
                    if board[k][h] !='B':
                        w+=1
                    if board[k][h] !='W':
                        b+=1
        result.append(min(b, w))
print(min(result))
                    
