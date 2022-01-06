a,b=list(map(int,input().split()))
afac=1
bfac=1
cfac=1

for i in range(a,0,-1): # 팩토리얼=입력받은 숫자를 내림차순으로 곱하기
    afac=afac*i    

for i in range(b,0,-1):
    bfac=bfac*i    
    
for i in range(a-b,0,-1):
    cfac=cfac*i    

print(afac//(bfac*cfac))
