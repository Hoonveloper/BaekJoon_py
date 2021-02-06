import sys 
input=sys.stdin.readline
from collections import deque

def dfs(matrix, v, visited):
    visited[v]=True
    print(v,end=' ') #출발점 방문처리, 출력
    for i,value in enumerate(matrix[v]): 
        if value==1 and visited[i]==False: #인접행렬 값이 1이고  방문을 하지 않았으면 dfs함수 호출.
            dfs(matrix,i,visited)

def bfs (matrix, start, visited):
    queue=deque([start]) #deque에 출발점 추가하면서 queue생성.
    while queue:
        v= queue.popleft() 
        if visited[v]==True: continue
        visited[v]=True
        print(v,end=' ')
        for i,value in enumerate(matrix[v]): 
            if value ==1 and visited[i]==False: 
                queue.append(i)

##인접행렬 구현 좌,우 대칭으로
n,m,v=map(int , input().split()) #n,m,v 입력
matrix=[ [0]*(n+1) for _ in range(n+1) ] # _은 무시하는 역할 (여기서는 index 무시)
graph= []
for i in range(m):
    z,x=map(int,input().split())
    matrix[z][x]=1
    matrix[x][z]=1


visited= [False]* (n+1)
dfs(matrix,v,visited)
visited= [False]* (n+1) #visited 값 초기화
print() #한 줄 띄우기 
bfs(matrix,v,visited)

