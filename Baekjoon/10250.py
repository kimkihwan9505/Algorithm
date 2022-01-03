f = int(input())
for _ in range(f):
    a,b,c = map(int,input().split())
    floor = c%a # 101,201,301~601,102,202,302,402 에서 층만
    room=c//a +1 # 101,201,301~601,102,202,302,402 10//6 =1 1호실은 꽉찼으니까 다음호실
    if floor ==0 :
        floor=a
        room=c//a
    print(floor*100+room)
