from collections import defaultdict as dd
from typing import List, Dict, Tuple
from pprint import pprint
import string
import re

from utils import stream_lines

file = 'prob13.in'
lines = [line.strip('\r\n') for line in open(file).readlines()]

dot_map: set[Tuple[int,int]] = set()
for line in lines:
  if line == '':
    break
  x,y = map(int, line.split(','))
  dot_map.add((x,y))

folds = []
for line in reversed(lines):
  if line == '':
    break
  parts = line.split(' ')
  main_part = parts[-1]
  folds.insert(0, main_part.split('='))

def handle_fold(dot_map: set[Tuple[int,int]], fold: Tuple[str,str]):
  next_map = set()
  if fold[0] == 'x':
    for dot in dot_map:
      xline = int(fold[1])
      next_map.add((abs(dot[0] - xline), dot[1]))
  else:
    for dot in dot_map:
      yline = int(fold[1])
      next_map.add((dot[0], abs(dot[1] - yline)))

  return next_map


first_fold = handle_fold(dot_map, folds[0])
print(len(first_fold))


