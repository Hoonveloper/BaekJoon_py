import sys
input=sys.stdin.readline
num= int(input())
queue=list()
order=list()
back=-1
front= -1
size=-1


for i in range(num):
    
    order=input().split()
    if order[0].lower() =="push":
        #print(1)
        queue.append(order[1])
        size+=1
        #print(queue)
    elif order[0].lower()=='pop':
        #비었을 때
        if size==-1:
            print(-1)
        else:
            print(queue[0])
            del queue[0]
           
            size-=1
    elif order[0].lower()=='size':
        print(size+1)
    elif order[0].lower()=='empty':
        if size==-1 : print(1)
        else :print(0)
    elif order[0].lower()=='front':
        #비었을 경우
        if size==-1: print(-1)
        else: print(queue[0])
    elif order[0].lower()=='back':
        if size==-1: print(-1)
        else: print(queue[size])

    
    