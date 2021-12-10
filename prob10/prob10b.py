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

  return opens

points = {"(": 1, "[": 2, "{": 3, "<":4}
def calc_score(opens):
  s = 0
  for item in reversed(opens):
    s *= 5
    s += points[item]
  return s



scores = []

for line in lines:
  val = check_legality(line)
  if val is sentinel or val in pairs.values():
    continue
  assert type(val) == type([])
  scores.append(calc_score(val))
  

l = len(scores)
sorted_scores = list(sorted(scores))
print(sorted_scores[l//2])
