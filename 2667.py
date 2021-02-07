import sys

n= int(input())
dx=[0,0,1,-1]
dy=[-1,1,0,0]
house_nums=[]
house_num=0
danji=0
visited=[ [False] *n for _ in range(n) ]
matrix= []
for _ in range(n):
    matrix.append(list(map(int,input())))


def dfs(y,x):
    global house_num
    visited[y][x]=True
    if matrix[y][x]==1:
        house_num+=1
        
    #print("집 수: {}".format(house_num))
   # print("현재 위치: {}{}".format(y,x))
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        #print("다음 탐색 위치:{}{}".format(ny,nx))
        if 0<=ny<n and 0<=nx<n:
            if matrix[ny][nx] == 1 and visited[ny][nx]==False:
                dfs(ny,nx)

for i in range(n):
    for j in range(n):
        if matrix[i][j]==1 and visited[i][j]==False:
            dfs(i,j)
            danji+=1
            house_nums.append(house_num)
            house_num=0
print(len(house_nums))
house_nums.sort()
for i in house_nums:
    print(i)