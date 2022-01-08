import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)
            
 '''
 input으로 받고 리스트를 만들고 append 하면 메모리 초과로 실패한다
 범위가 10000까지 이기 때문에 10001 까지 먼저 리스트를 만들고 
 그뒤에 받는수를 더한다 
 '''
