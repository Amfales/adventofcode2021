from collections import defaultdict as dd
from typing import List, Dict, Tuple
from pprint import pprint
import string

from utils import stream_lines

file = 'prob13.in'
#file = 'scratch.txt'
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
      next_map.add((dot[0], yline - abs(dot[1] - yline)))

  return next_map

def print_dots(dot_map):
  len1,len2 = max([x[0] for x in dot_map]), max([x[1] for x in dot_map])
  grid = [["." for x in range(len1+1)] for y in range(len2+1)]
  for item in dot_map:
    grid[item[1]][item[0]] = '*'

  print('\n'.join([''.join(line) for line in grid]))

test_map = dot_map
for fold in folds:
  print_dots(test_map)
  print()
  test_map = handle_fold(test_map, fold)

print_dots(test_map)
