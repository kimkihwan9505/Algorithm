a= int(input())
tmp=[]
for _ in range(a):
    string=input()
    tmp.append(string)

for i in sorted(set(tmp), key=lambda x:(len(x), x)): #리스트 중복 제거를 set으로 하고 정렬->key=lamda x:(우선순위,차선)
    print(i)
    
    
