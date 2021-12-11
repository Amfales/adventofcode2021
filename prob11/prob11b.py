from collections import defaultdict as dd
from typing import List
from pprint import pprint

from utils import stream_lines

file = 'prob11.in'
lines = [[int(x) for x in line] for line in stream_lines(file)]

def process_day(grid):
  len1,len2 = len(grid),len(grid[0])
  def get_adjacents(x,y):
    diffs = [(a,b) for a in (-1,0,1) for b in (-1,0,1) if (a,b) != (0,0)]
    return [(first, second)
            for a in diffs 
            if 0 <= (first := x+a[0]) < len1 and
            0 <= (second := y+a[1]) < len2]

  next_grid = [[x+1 for x in line] for line in grid]
  flashed = set()
  last_changed = False
  while True:
    for x in range(len1):
      for y in range(len2):
        if next_grid[x][y] > 9 and (x,y) not in flashed:
          last_changed = True
          flashed.add((x,y))
          next_grid[x][y] = 0
          for x1,y1 in get_adjacents(x,y):
            if (x1,y1) not in flashed:
              next_grid[x1][y1] += 1
          
    if not last_changed:
      break
    last_changed = False

  return next_grid,flashed


mid_grid = [line[:] for line in lines]
s = 0
for x in range(100000):
  next_grid,flashed = process_day(mid_grid)
  if len(flashed) == 100:
    print(x+1)
    break
  mid_grid = next_grid
