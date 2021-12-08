from collections import defaultdict as dd
from typing import List

from utils import stream_lines


lines = []
for line in stream_lines('prob08.in'):
  parts = line.split(' | ')
  lines.append((parts[0].split(' '), parts[1].split(' ')))

s = 0
for line in lines:
  for item in line[1]:
    if len(item) in (2,4,3,7):
      s += 1

print(s)