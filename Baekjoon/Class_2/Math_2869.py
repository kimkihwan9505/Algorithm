a,b,c=map(int,input().split())
day=(c-a)/(a-b)+1
print(int(day)) if day == int(day) else print(int(day)+1)
#---------------------------------------------
c=(a-b)*n+a
n=(c-a)/(a-b)
마지막에 a만큼 올라간 날을 빼주어서 날짜 기준으로는 하루를 뺀 것과 같기 때문에 +1을 해주었다
