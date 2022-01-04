while 1:
    a = list(map(int,input().split()))
    max_a=max(a) #최대값 지정
    a.remove(max_a) #최댓값을 리스트에서 뺀다
    if sum(a)==0: break #0이면 종료
    if a[0]**2+a[1]**2==max(a)**2: # 피타고라스정리
        print('right')
    else:
        print('wrong')
----------------------------------------
