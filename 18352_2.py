import sys
from collections import deque
input=sys.stdin.readline
n,m,k,x=map(int,input().split())
answer=[-1] * (n+1)
answer[x]=0
path = [[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    path[a].append(b)
#print(path)
#rint(answer)
queue = deque([x])

while queue:
    now=queue.popleft()
    for nxt in path[now]:
        if answer[nxt]==-1:
            answer[nxt]=answer[now]+1        
            queue.append(nxt)
isExist=False
real_answer=[]
#print(answer)
for idx,val in enumerate(answer):
    #print(idx)
    if val==k:
        #print("ㄱㅌ")
        real_answer.append(idx)
        #print(real_answer)
        isExist=True
if isExist==False:
    print(-1)
else:
    real_answer.sort()
    for i in real_answer:
        print(i)