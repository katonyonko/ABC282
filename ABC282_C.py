import io
import sys

_INPUT = """\
6
8
"a,b"c,d
5
,,,,,
20
a,"t,"c,"o,"d,"e,"r,
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  S=input()
  ans=[]
  flg=0
  for i in range(N):
    if flg==0 and S[i]==',': ans.append('.')
    else: ans.append(S[i])
    if S[i]=='"': flg^=1
  print(''.join(ans))