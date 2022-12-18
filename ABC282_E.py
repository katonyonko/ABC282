import io
import sys

_INPUT = """\
6
4 10
4 2 3 2
20 100
29 31 68 20 83 66 23 84 69 96 41 61 83 37 52 71 18 55 40 8
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  #Kruskal法 max_vに頂点数,edgesに辺(重み、結んでいる２つの頂点（順不同）で入れる)
  class UnionFind():
    def __init__(self, n):
      self.n = n
      self.parents = [-1] * n
    def find(self, x):
      if self.parents[x] < 0:
        return x
      else:
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self, x, y):
      x = self.find(x)
      y = self.find(y)
      if x == y:
        return
      if self.parents[x] > self.parents[y]:
        x, y = y, x
      self.parents[x] += self.parents[y]
      self.parents[y] = x
    def size(self, x):
      return -self.parents[self.find(x)]
    def same(self, x, y):
      return self.find(x) == self.find(y)
    def members(self, x):
      root = self.find(x)
      return [i for i in range(self.n) if self.find(i) == root]
    def roots(self):
      return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
      return len(self.roots())
    def all_group_members(self):
      return {r: self.members(r) for r in self.roots()}
    def __str__(self):
      return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
  def Kruskal(G):
    edges=set()
    for i in range(len(G)):
      for j in range(len(G[i])):
        c,k=G[i][j]
        l,m=min(i,k),max(i,k)
        edges.add((c,l,m))
    edges=list(edges)
    edges.sort()
    uf = UnionFind(len(G))
    mst = [] #最小全域木の辺すべて
    weight=0 #最小全域木の重さ
    for edge in edges:
      if not uf.same(edge[1], edge[2]):
        uf.union(edge[1], edge[2])
        mst.append(edge)
        weight+=edge[0]
    return mst,weight

  N,M=map(int,input().split())
  A=list(map(int,input().split()))
  score=[(pow(A[i],A[j],M)+pow(A[j],A[i],M))%M for i in range(N) for j in range(N)]
  G=[[] for _ in range(N)]
  for i in range(N):
    for j in range(i+1,N):
      G[i].append((-score[i*N+j],j))
      G[j].append((-score[i*N+j],i))
  print(-Kruskal(G)[1])