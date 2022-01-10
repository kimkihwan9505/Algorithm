import sys

a= int(sys.stdin.readline())

stack = []

for _ in range(a):
    cmd=sys.stdin.readline().split()

    if cmd[0] == 'push_front':
        stack.insert(0,cmd[1])

    elif cmd[0] =='push_back':
        stack.append(cmd[1])

    elif cmd[0] =='pop_front':
        if len(stack) ==0:
            print(-1)
        else :
            print(stack.pop(0))

    elif cmd[0] == 'pop_back':
        if len(stack) ==0:
            print(-1)
        else :
            print(stack.pop())
    elif cmd[0] =='size':
        print(len(stack))

    elif cmd[0] =='empty':
        if len(stack) ==0:
            print(1)
        else :
            print(0)
    elif cmd[0] =='front':
        if len(stack)==0:
            print(-1)
        else :
            print(stack[0])

    elif cmd[0] =='back':
        if len(stack)==0:
            print(-1)
        else :
            print(stack[-1])
