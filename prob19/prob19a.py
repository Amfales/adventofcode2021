import copy
from functools import lru_cache
import re
import string
from collections import defaultdict as dd
from pprint import pprint
from typing import Dict, Generator, List, Mapping, Optional, Tuple
import statistics

from utils import stream_lines

#@lru_cache(maxsize=1000)
def distance(pt1, pt2) -> float:
  return ((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2 + (pt1[2] - pt2[2])**2)**(0.5)

def pairwise_match(scanners):
  for x in range(len(scanners)):
    for y in range(x+1, len(scanners)):
      yield (scanners[x],scanners[y])

def has_matching_distance(scanners, dist: float):
  for x1,x2 in pairwise_match(scanners):
    if (distance(x1,x2) - dist) < 1e-4:
      return True
  return False

def get_corresponding_dists(scanners, idxs: list[int]) -> dict[tuple[int,int],float]:
  dists = dict()
  for idx1 in idxs:
    for idx2 in idxs:
      if idx1 != idx2:
        dists[(idx1,idx2)] = distance(scanners[idx1],scanners[idx2])
  return dists







file = 'prob19.in'
#file = 'scratch.txt'
groups = open(file).read().strip().split('\n\n')
scan_lookup:  Mapping[int, list[tuple[int,int,int]]] = dd(list)
for i, group in enumerate(groups):
  scanners = group.split('\n')[1:]
  for scanner in scanners:
    data = tuple(map(int, scanner.split(',')))
    scan_lookup[i].append(data)
    


# scanner_num -> internal_beacon_num -> other_beacon_num -> distance
closeness: Mapping[int, Mapping[int, Mapping[int, float]]] = dd(lambda: dd(lambda: dd(float)))
s_num = 0
for s in range(len(scan_lookup)):
  for x in range(len(scan_lookup[s])):
    for y in range(x+1, len(scan_lookup[s])):
      d = distance(scan_lookup[s][x], scan_lookup[s][y])
      closeness[s][x][y] = d
      closeness[s][y][x] = d
    

# scanner_num -> internal_beacon_num -> list(i,(a,b,c))
distances_lookup = dd(lambda: dd(list))
for s in range(len(scan_lookup)):
  for x in range(len(scan_lookup[s_num])):
    distances_lookup[s][x] = sorted(list(enumerate(scan_lookup[s][:])), key=lambda w: closeness[s][x][w[0]])
  

dl =  distances_lookup

small = None
idx = -1
start = 0
for x in range(len(scan_lookup[s_num])):
  pt1,pt2 = dl[start][x][0],dl[start][x][1]
  print(pt1)
  dist = closeness[s_num][pt1[0]][pt2[0]]
  if small is None or dist < small:
    small = dist
    idx = x
    
print(small)
print(idx)

print(dl[0][5])
dists = get_corresponding_dists(scan_lookup[0], [5,14,18])
print(dists)

for s in range(len(scan_lookup)):
  if s != 0: #We're based out of scanner 0
    if has_matching_distance(scan_lookup[s], small):
      print(s)
