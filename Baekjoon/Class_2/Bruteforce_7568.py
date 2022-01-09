a = int(input())
info = [list(map(int, input().split())) for _ in range(a)]
for i in info:
    rank=1
    for j in info:
        if i[0] < j[0] and i[1]<j[1]: #키를 비교 하고 몸무게도 비교 해서 큰사람이 존재하면 +1
            rank+=1
    print(rank,end=' ') # 출력값 주의 
