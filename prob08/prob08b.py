from collections import defaultdict as dd
from typing import List
from pprint import pprint

from utils import stream_lines


lines = []
for line in stream_lines('prob08.in'):
  parts = line.split(' | ')
  lines.append((parts[0].split(' '), parts[1].split(' ')))


def get_zero(partial: dict[int, set], num_map: dict[int, List[set]]):
  mid_and_left = partial[4] - partial[1]
  for item in num_map[6]:
    mix = mid_and_left.intersection(item)
    if len(mix) != 2:
      partial[0] = item

def get_six_and_nine(partial: dict[int, set], num_map: dict[int, List[set]]):
  assert (partial[0] is not None)
  assert (partial[1] is not None)
  for item in num_map[6]:
    mix = partial[1].intersection(item)
    if len(mix) == 1:
      partial[6] = item
    elif not partial[0].issubset(item):
      partial[9] = item

def get_five(partial: dict[int, set], num_map: dict[int, List[set]]):
  assert (partial[6] is not None)
  for item in num_map[5]:
    mix_six = partial[6].intersection(item)
    mix_one = partial[1].intersection(item)
    if len(mix_one) == 2:
      partial[3] = item
    elif len(mix_six) == 5:
      partial[5] = item
    else:
      partial[2] = item




def get_mapping(mapping: List[set]):
  m: dict[int,set] = {x:None for x in range(1,10)}
  num_map: dict[int, List[set]] = {}
  for item in mapping:
    item_len = len(item)
    if item_len not in num_map:
      num_map[item_len] = [item]
    else:
      num_map[item_len].append(item)

  m[8] = num_map[7][0]
  m[1] = num_map[2][0]
  m[4] = num_map[4][0]
  m[7] = num_map[3][0]

  get_zero(m, num_map)
  get_six_and_nine(m, num_map)
  get_five(m, num_map)
  return m

def inverse_mapping(mapping: dict[int, set]):
  def inner(key: str):
    for item in mapping:
      group = mapping[item]
      if len(key) == len(group) and all([x in group for x in key]):
        return item
    return -1
  return inner

def out_to_num(mapping: dict[int, set], output: list[str]):
  i = 0
  rev_mapping = inverse_mapping(mapping)
  for item in output:
    i *= 10
    i += rev_mapping(item)
  return i

  

s = 0
for line in lines:
  key = [set(x) for x in line[0]]
  mapping = get_mapping(key)
  val = out_to_num(mapping, line[1])
  s += val

print(s)

  
  