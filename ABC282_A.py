import io
import sys

_INPUT = """\
6
3
1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  K=int(input())
  s=''.join([chr(ord('A')+i) for i in range(26)])
  print(s[:K])