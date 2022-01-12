a =int(input())
num=[]
for _ in range(a):
    b=int(input())
    if b ==0:
        num.pop()
    else:
        num.append(b)
print(sum(num))
'''
b를 다입력받고 탐색으로 0 일때 pop을 하니까 시간 초과 남
'''
