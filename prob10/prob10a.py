from collections import defaultdict as dd
from typing import List
from pprint import pprint

from utils import stream_lines

file = 'prob10.in'
lines = [line for line in stream_lines(file)]

pairs = {"(": ")", "[":"]","{":"}","<":">"}
sentinel = object()

def check_legality(line):
  idx = 0
  l = len(line)
  opens = []
  while idx < l:
    char = line[idx]
    if char in pairs.keys():
      opens.append(char)
    elif char in pairs.values():
      if not opens or char != pairs[opens[-1]]:
        return char
      elif not opens:
        return sentinel
      else:
        opens.pop()
    else:
      return char
    idx += 1

  return None


counts = dd(int)
points = {")": 3, "]": 57, "}": 1197, ">":25137}
for line in lines:
  val = check_legality(line)
  if val is not sentinel and val is not None:
    counts[val] += 1

s = 0
for item in counts:
  s += (points[item] * counts[item])

print(s)
