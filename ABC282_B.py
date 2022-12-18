import io
import sys

_INPUT = """\
6
5 5
ooooo
oooxx
xxooo
oxoxo
xxxxx
3 2
ox
xo
xx
2 4
xxxx
oxox
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  S=[input() for _ in range(N)]
  ans=0
  for i in range(N):
    S[i]=sum([1<<j if S[i][j]=='o' else 0 for j in range(M)])
  for i in range(N):
    for j in range(i+1,N):
      if S[i]|S[j]==(1<<M)-1: ans+=1
  print(ans)