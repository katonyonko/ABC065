from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="065"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc076_b".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
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
  N=int(input())
  city=[list(map(int,input().split())) for _ in range(N)]
  city=[(city[i][0],city[i][1],i) for i in range(N)]
  uf=UnionFind(N)
  kouho=[]
  city.sort(key=lambda x: x[0])
  for i in range(N-1):
    kouho.append((city[i+1][0]-city[i][0],city[i][2],city[i+1][2]))
  city.sort(key=lambda x: x[1])
  for i in range(N-1):
    kouho.append((city[i+1][1]-city[i][1],city[i][2],city[i+1][2]))
  kouho.sort(key=lambda x: x[0])
  ans=0
  for i in range(2*(N-1)):
    if uf.size(0)==N: break
    d,x,y=kouho[i]
    if uf.find(x)!=uf.find(y):
      ans+=d
      uf.union(x,y)
  print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])