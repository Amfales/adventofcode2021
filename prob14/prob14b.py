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
  mapping[parts[0]] = parts[1]


def handle_insert(group: str, mapping: dict[str,str]) -> str:
  next_str = group[0]
  for a,b in zip(group, group[1:]):
    if f"{a}{b}" in mapping:
      next_str += mapping[f"{a}{b}"] + b

  return next_str

def handle_insert_good(group: dict[tuple[str,str],int], mapping: dict[tuple[str,str],str]) -> str:
  next_group = dd(int)
  for item in group:
    if item in mapping:
      letter = mapping[item]
      next_group[(item[0], letter)] += group[item]
      next_group[(letter, item[1])] += group[item]

  return next_group



last_letter = group[-1]
num_steps = 40
temp_group = dd(int)
for a,b in zip(group, group[1:]):
  temp_group[(a,b)] += 1


temp_mapping = {tuple(a): mapping[a] for a in mapping}

for x in range(num_steps):
  temp_group = handle_insert_good(temp_group, temp_mapping)

#pprint(temp_group)
all_letters = set(temp_mapping.values())
big = 0
for letter in all_letters:
  s = 0 if letter != last_letter else 1
  for item in temp_group:
    if letter == item[0]:
      s += temp_group[item]

  big = max(big,s)

little = float('inf')
for letter in all_letters:
  s = 0 if letter != last_letter else 1
  for item in temp_group:
    if letter == item[0]:
      s += temp_group[item]

  little = min(little,s)


print(big - little)


