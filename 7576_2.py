from collections import deque
n,m= map(int, input().split())
dy=[-1,1,0,0]
dx=[0,0,-1,1]
#그래프 저장
graph=[ list(map(int, input().split())) for _ in range(m)  ]
queue=deque()
for i in range(m):
    for j in range(n):
        if graph[i][j]==1:
            queue.append((i,j))

while queue:
    y,x=queue.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if graph[ny][nx]==0:
                graph[ny][nx]=graph[y][x]+1
                queue.append((ny,nx))
            
isTrue=True # True면 다 익은 토마토 맵, false면 이상한 맵
answer=-100
for i in range(m):
    for j in range(n):
        if graph[i][j]==0: #안익은 토마토 있는 경우.
            isTrue=False
            answer=-1
            break
        answer =max(answer,graph[i][j])

    if isTrue==False:break

if answer!= -1 : 
    answer-=1
print(answer)