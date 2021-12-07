from collections import defaultdict as dd
from typing import List

from utils import stream_lines


line = list(stream_lines('prob07.in'))[0]
nums = list(map(int, line.split(',')))

top,bottom = min(nums),max(nums)

def triangle(n):
  return (n*(n+1))/2


def calc_fuel(nums, num):
  s = 0
  for v in nums:
    s += triangle(abs(v - num))
  return s

best = float('inf')
for val in range(top, bottom+1):
  small = calc_fuel(nums, val)
  if small < best:
    best = small

print(best)

