import sys
n= int(input())
stack=list()
point=-1
for i in range(n):
    lst=list(input().split())
    if lst[0].lower()=="push":
        stack.append(lst[1])
        point+=1
        
    elif lst[0].lower()=="pop":
        #길이 체크
        if point <0: print(-1)
        else:
            print(stack[point])
            del stack[point]
            point-=1
    elif lst[0].lower()=="size":
        print(point+1)
    elif lst[0].lower()=="empty":
        print(1) if point==-1 else print(0)
    elif lst[0].lower()=="top":
        if point <0: print(-1)
        else: print(stack[point])



