num= int(input())
floor=100
room=1
for i in range(num):
    floor=100
    room=1
    h,w,n=input().split()
    h=int(h)
    w=int(w)
    n=int(n)
   
    
    floor= n%h+1
    room= int(n/h)
    
    print(room,floor)
    