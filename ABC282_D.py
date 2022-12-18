import io
import sys

_INPUT = """\
6
5 4
4 2
3 1
5 2
3 2
4 3
3 1
3 2
1 2
9 11
4 9
9 1
8 2
8 3
9 2
8 4
6 7
4 6
7 5
4 5
7 8
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  inf=10**30
  def bfs(G,s):
    o,e=0,1
    parent[s]=s
    D[s]=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if D[y]<inf and D[x]%2==D[y]%2: return -1,-1
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
          if D[x]%2==0: o+=1
          else: e+=1
          parent[y]=s
    return o,e

  N,M=map(int,input().split())
  G=[[] for _ in range(N)]
  for i in range(M):
    u,v=map(lambda x: int(x)-1,input().split())
    G[u].append(v)
    G[v].append(u)
  D=[inf]*len(G)
  parent=[-1]*len(G)
  tmp={}
  flg=0
  for i in range(N):
    if D[i]<inf: continue
    o,e=bfs(G,i)
    if o==-1 and e==-1: flg=1; break
    tmp[i]=(o,e)
  if flg==1: print(0)
  else:
    ans=0
    for i in range(N):
      if D[i]%2==0:
        ans+=N-len(G[i])-tmp[parent[i]][1]
      else: ans+=N-len(G[i])-tmp[parent[i]][0]
    print(ans//2)