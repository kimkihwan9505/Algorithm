chess=[]
for _ in range(8):
    chess.append(list(map(str,input())))    
cnt=0
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            if chess[i][j] =='a':
                cnt+=1
print(cnt)            
