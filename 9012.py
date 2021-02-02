import sys
input=sys.stdin.readline
n=int(input())

stack=list()
p=-1
flag=True #false:거짓 아님(참)
for i in range(n):
    data=input()
    l=len(data)
    p=-1
    flag=True
    stack.clear()
    for j in range(l):
        
       # print("현재값 {}".format(data[j]))
        if p==-1 and data[j]==')': 
            flag=False
            #print(0)
            break
        
        elif data[j]=='(':
            stack.append(data[j])
            p+=1
           # print(1)
        elif data[j]==')':
            del stack[p]
            p-=1
           # print(2)
   # print("플래그 {} , p {} , stack {}".format(flag,p,stack))
    if p==-1 and flag==True: 
       print("YES")
       continue

    print("NO")
   
       
    
    