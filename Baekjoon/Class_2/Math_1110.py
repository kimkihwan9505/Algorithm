
num = int(input())
check = num
new_num = 0
temp = 0
count = 0
while True:
    temp = num//10 + num%10
    new_num = (num%10)*10 + temp%10
    count += 1
    num = new_num
    if new_num == check:
        break
print(count)



'''
시간초과(str)
a=input()
b=a
cnt=0
while 1:
    if len(b) ==1:
        b="0"+b
    c=str(int(b[0])+int(b[1]))
    b=b[-1]+c[-1]
    cnt+=1
    if a == b:
        print(cnt)
        break
'''
