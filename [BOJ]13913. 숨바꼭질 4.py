from collections import deque

n,k=map(int,input().split())
visited=[0]*100001
graph=[0]*100001
def bfs():
    queue=deque([n])
    while queue:
        x=queue.popleft()
        if x==k:
            print(visited[x])
            p=[]
            while x!=n:
                p.append(x)
                x=graph[x]
            p.append(n)
            p.reverse()
            print(' '.join(map(str,p)))
            return
        location=[x-1,x+1,x*2]
        for l in location:
            if 0<=l<=100000 and visited[l]==0:
                visited[l]=visited[x]+1
                graph[l]=x
                queue.append(l)

bfs()

