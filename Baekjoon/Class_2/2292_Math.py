a=int(input())
num=1 # 처음 시작 하는 곳
cnt =1 # 반복하는 횟수 
while a >num:
    num+=6*cnt # 6의 배수로 돈다 
    cnt+=1 
print(cnt)
