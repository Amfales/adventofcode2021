from collections import defaultdict as dd
from typing import List

from utils import stream_lines


all_lines = list(stream_lines('prob05.in'))

all_points = [
  [list(map(int, x.split(','))) for x in line.split('->')]
  for line in all_lines
]

straight_lines = list(
  filter(
    lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1],
    all_points
  )
)

sub_map = dd(int)
for line in straight_lines:
  x1,y1 = line[0]
  x2,y2 = line[1]
  if x1 == x2:
    y_start, y_end = min(y1,y2), max(y1,y2)
    for z in range(y_end-y_start+1):
      sub_map[(x1, y_start+z)] += 1

  elif y1 == y2:
    x_start, x_end = min(x1,x2), max(x1,x2)
    for z in range(x_end-x_start+1):
      sub_map[(x_start + z, y1)] += 1

print(sum([1 for x in sub_map if sub_map[x] > 1]))

  



#print(len(all_points), len(straight_lines))