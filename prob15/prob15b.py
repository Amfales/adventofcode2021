from collections import defaultdict as dd
from typing import List, Dict, Tuple
from pprint import pprint
import string
import heapq as hq
import re

from utils import stream_lines

file = 'prob15.in'
#file = 'scratch.txt'
lines = [[int(x) for x in line.strip()] for line in open(file).readlines() if line != '\n']

big_lines = [[0 for x in range(5*len(lines[0]))] for y in range(5*len(lines))]


for big_x in range(5):
  for big_y in range(5):
    for x in range(len(lines)):
      for y in range(len(lines[0])):
        val = lines[x][y] + big_x + big_y
        while val >= 10:
          val -= 9
        big_lines[big_x*len(lines) + x][big_y*len(lines[0]) + y] = val


def nb(grid, x, y):
  diffs = zip((0,0,1,-1), (1,-1,0,0))
  return [(first, second) for d in diffs if 0 <= (first := x+d[0]) < len(grid) if 0 <= (second := y+d[1]) < len(grid[0])]

def dijkstra(grid: list[list[int]]):
  br = (len(grid) - 1, len(grid[0]) - 1)
  pq = [(0,(0,0))]
  seen = set()
  while pq:
    dist, loc = hq.heappop(pq)
    if loc in seen:
      continue
    seen.add(loc)
    if loc == br:
      return dist
    for n in nb(grid,loc[0],loc[1]):
      hq.heappush(pq, (dist+grid[n[0]][n[1]], n))

  
dist = dijkstra(big_lines)
print(dist)