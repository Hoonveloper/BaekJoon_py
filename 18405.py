import sys
input =sys.stdin.readline
from collections import deque
input=sys.stdin.readline

n,k= map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n) ]
s,x,y=map(int, input().split())
print(graph)
queue=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]!= 0 :
            queue.append([ graph[i][j], i,j, 0] )
queue.sort() #정렬 먼저 해주고 deque만들기
#여기서는 정렬먼저 해주고 하면 바이러스 level 비교 필요 x
# 낮은게 먼저 들어가니까 비교 할 필요가 없어진다.
queue=deque(queue)
#print(queue)
dy=[0,0,-1,1]
dx=[1,-1,0,0]
while queue:
    v,a,b,time=queue.popleft()
    if time==s:
        break
    else:
        for i in range(4):
            na=a+dy[i]
            nb=b+dx[i]
            if 0<=na<n and 0<=nb< n:
                if graph[na][nb]==0:
                    graph[na][nb]=v
                    queue.append([v,na,nb,time+1])

print(graph[x-1][y-1])