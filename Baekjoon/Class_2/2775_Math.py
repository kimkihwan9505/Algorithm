
t= int(input())

for i in range(t):
    k=int(input())
    n=int(input())
    people=[i for i in range(1,n+1)] # 0층 사람수기준으로 
    
    for j in range(k):
        for h in range(1,n):
            people[h]+=people[h-1]
    print(people[-1])
