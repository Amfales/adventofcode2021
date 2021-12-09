from collections import defaultdict as dd
from typing import List
from pprint import pprint

from utils import stream_lines

def is_lowpoint(lines, pt):
  len1, len2 = len(lines), len(lines[0])
  x,y = pt
  non_diag_diffs = [(0,1), (0,-1), (-1,0), (1,0)]
  non_diag_pts = [(x+a[0],y+a[1]) for a in non_diag_diffs]
  diffs = [(x+a,y+b) for a in (-1,0,1) for b in (-1,0,1) if not (a == 0 and b==0)]
  for point in non_diag_pts:
    if point[0] < 0 or point[0] >= len1:
      continue
    if point[1] < 0 or point[1] >= len2:
      continue
    
    if lines[point[0]][point[1]] <= lines[x][y]:
      return False
  
  return True


file = 'prob09.in'
lines = [[int(x) for x in line] for line in stream_lines(file)]
len1, len2 = len(lines), len(lines[0])
print(len1,len2)
s = 0
m = [[False for y in range(len2)] for x in range(len1)]
ct = 0
for x in range(len1):
  for y in range(len2):
    if is_lowpoint(lines, (x,y)):
      s += (lines[x][y] + 1)
      #print((x,y))
      m[x][y] = True
      ct += 1


print(s)