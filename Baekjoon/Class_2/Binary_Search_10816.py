N= int(input())
cards=list(map(int,input().split()))
cards.sort()
cardsDic={}
for c in cards:
    if c not in cardsDic:
        cardsDic[c]=1     # 가지고 있는 카드의 갯수와 값을 딕셔너리로 받음 -> 찾고자 하는 숫자 검색하기전 value 값을 이미 구함 
    else:
        cardsDic[c]+=1
        
M=int(input())
num=list(map(int,input().split()))

for i in num:
    if i in cardsDic: #같은 key값으로 검색 해서 있으면 value 출력
        print(cardsDic[i],end=' ') 
    else :
        print(0,end=' ')
