from collections import defaultdict as dd
from typing import List, Dict, Tuple
from pprint import pprint
import string
import re

from utils import stream_lines

file = 'prob15.in'
#file = 'scratch.txt'
lines = [[int(x) for x in line.strip()] for line in open(file).readlines()]
best = [line[:] for line in lines]

for x in range(len(lines)):
  for y in range(len(lines[0])):
    if x == 0 or y == 0:
      if y != 0:
        best[x][y] = best[x][y] + best[0][y-1]
      elif x != 0:
        best[x][y] = best[x][y] + best[x-1][0]
      else:
        best[x][y] = best[x][y]
        continue
    else:
      best[x][y] = best[x][y] + min(best[x-1][y], best[x][y-1])


print(best[-1][-1] - best[0][0])
