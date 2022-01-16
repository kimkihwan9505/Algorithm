
a,b = map(int,input().split())
sreach={}
for _ in range(a):
    site,ps = input().split()
    sreach[site]=ps #리스트를 해시로 변환 키, 벨류
for _ in range(b):
    print(sreach[input()])
