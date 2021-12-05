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
for line in all_points:
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

  else:
    
    left_x = min(x1,x2)
    left_y = y1 if left_x == x1 else y2

    right_x = x1 if left_x == x2 else x2
    right_y = y1 if left_y == y2 else y2

    #print([x1,y1,x2,y2],[left_x, left_y, right_x, right_y])

    if left_y < right_y:
      for z in range(right_x - left_x + 1):
        sub_map[(left_x + z, left_y + z)] += 1
    else:
      for z in range(right_x - left_x + 1):
        sub_map[(left_x + z, left_y - z)] += 1


print(sum([1 for x in sub_map if sub_map[x] > 1]))

max_x = -1; max_y = -1
for line in all_points:
  max_x = max(max_x, line[0][0], line[1][0])
  max_y = max(max_y, line[0][1], line[1][1])

#print('\n'.join(all_lines))

"""
for y in range(max_y+5):
  for x in range(max_x+5):
    if sub_map[(x,y)] > 0:
      print(sub_map[(x,y)], end='')
    else:
      print('.', end='')
  print()
"""
  



#print(len(all_points), len(straight_lines))