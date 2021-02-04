n,k=map(int , input().split())
# map으로 한번에 int로 캐스팅 해줌 
print(n,k)
num=0
res=list()
arr=[i*3 for i in range(1,n+1)]
print(arr)

for j in range(n):
    num=num+k-1
    if num>= len(arr):
        num=num%len(arr)
    res.append(arr[num])
    arr.pop(num)
    
print(res)

