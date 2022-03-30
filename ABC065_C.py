from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="065"
#問題
problem="c"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc076_a".format(times, problem)) as res:
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
  mod=10**9+7
  N,M=map(int,input().split())
  if abs(N-M)>1: print(0)
  else:
    ans=1
    for i in range(N): ans=(ans*(i+1))%mod
    for i in range(M): ans=(ans*(i+1))%mod
    if abs(N-M)==0: ans=(ans*2)%mod
    print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])