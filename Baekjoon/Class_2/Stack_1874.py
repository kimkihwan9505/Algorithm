a=int(input())
op=[]
pre=[]
count=1
temp=True
for _ in range(a):
    num=int(input())
    while count <= num: # 입력받은 수 만큼 리스트에 추가 ,다음수가 하나 작은 수라도 count 조건에 걸리지 않기 때문에 바로 밑 if 문 수행
        pre.append(count)
        op.append('+')
        count+=1
        
    if pre[-1] == num: # 맨마지막수와 입력받은수를 비교 일치하면 pop. 같지않다면 수열을 만들수 없다 - > 
        pre.pop()
        op.append('-')
    else :
        temp=False
        break
if temp == False:
    print("NO")
else :
    for i in op:
        print(i)
