import io
import sys

_INPUT = """\
6
1
1
1 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  M=0
  d={}
  w=1
  ans=[]
  while w<=N:
    for i in range(N-w+1):
      M+=1
      d[(i,i+w-1)]=M
      ans.append((i+1,i+w))
    w*=2
  print(M)
  for i in range(M):
    print(*ans[i])
  Q=int(input())
  for _ in range(Q):
    L,R=map(lambda x: int(x)-1, input().split())
    w=1
    while w<=R-L+1: w*=2
    w//=2
    print(d[(L,L+w-1)],d[(R-w+1,R)])