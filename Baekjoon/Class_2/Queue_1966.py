t=int(input())

for _ in range(t):
    a,b = map(int,input().split())
    printlist = list(map(int,input().split()))
    checklist = [0 for _ in range(a)]
    checklist[b]=1 # 찾고싶은 순서를 1로 만든다 

    cnt = 0

    while 1:
        if printlist[0] == max(printlist):
            cnt +=1
            
            if checklist[0] != 1:
                printlist.pop(0)
                checklist.pop(0)
            else :
                print(cnt)
                break
            
        else :
            printlist.append(printlist.pop(0))
            checklist.append(checklist.pop(0))
            
     '''
     printlist 와 checklist의 길이를 같게 만들고 
     체크 리스트에 확인하고 싶은 인덱스에 값을 1 로 만들어주고 
     append 와 pop 연산을 독같이 해준다
     '''
