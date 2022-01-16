import sys 

m=int(sys.stdin.readline())
tmp=set()

for _ in range(m):
    commend=sys.stdin.readline().strip().split()
    if len(commend) ==1:
        if commend[0] =="all":
            tmp=set([i for i in range(1,21)])
        else :
            tmp=set()
    else :
        func,x = commend[0],commend[1]
        x=int(x)
        
        if func=="add":
            tmp.add(x)
        elif func=="remove":
            tmp.discard(x)
        elif func=="check":
            print(1 if x in tmp else 0)
        elif func=="toggle":
            if x in tmp:
                tmp.discard(x)
            else:
                tmp.add(x)
