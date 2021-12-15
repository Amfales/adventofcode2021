from collections import defaultdict as dd
from typing import List, Dict, Tuple
from pprint import pprint
import string
import re

from utils import stream_lines

file = 'prob14.in'
#file = 'scratch.txt'
group, things = open(file).read().split('\n\n')

mapping: dict[str,str] = dict()
for thing in things.split('\n'):
  if thing == '':
    continue
  parts = thing.strip().split(' -> ')
  print(parts)
  mapping[parts[0]] = parts[1]


def handle_insert(group: str, mapping: dict[str,str]) -> str:
  next_str = group[0]
  for a,b in zip(group, group[1:]):
    if f"{a}{b}" in mapping:
      next_str += mapping[f"{a}{b}"] + b

  return next_str


num_steps = 10
temp_group = group
for x in range(num_steps):
  temp_group = handle_insert(temp_group, mapping)

all_letters = set(temp_group)
big = max([temp_group.count(a) for a in all_letters])
little = min([temp_group.count(a) for a in all_letters])
print(big - little)


