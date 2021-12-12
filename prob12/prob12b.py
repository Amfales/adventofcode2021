from collections import defaultdict as dd
from typing import List, Dict
from pprint import pprint
import string

from utils import stream_lines

file = 'prob12.in'
lines = list(stream_lines(file))

mapping = dd(list)

for line in lines:
  a,b = line.split('-')
  mapping[a].append(b)
  mapping[b].append(a)

def is_small_cave(cave: str):
  return cave.lower() == cave

def is_big_cave(cave: str):
  return cave.upper() == cave

def get_all_paths(mapping: dict[str,list[str]]):
  paths = []
  part_paths = [(['start'], False)]
  while part_paths:
    cur_path, double_small = part_paths.pop()
    last_node = cur_path[-1]
    if last_node == 'end':
      paths.append(cur_path)
    else:
      for neighbor in mapping[last_node]:
        if neighbor == 'start':
          continue
        if is_small_cave(neighbor) and neighbor in cur_path:
          if not double_small:
            part_paths.append((cur_path[:] + [neighbor], True))
            continue
          else:
            continue
        part_paths.append((cur_path[:] + [neighbor], double_small))
  
  return paths


paths = get_all_paths(mapping)

print(len(paths))

