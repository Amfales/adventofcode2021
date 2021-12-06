from collections import defaultdict as dd
from typing import List

from utils import stream_lines



class LanternFish():
  def __init__(self, timer=8):
    self.timer = timer

fish_line = list(stream_lines('prob06.in'))[0]
fish = list(map(int, fish_line.split(',')))

fish_dict = dd(int)
for f in fish:
  fish_dict[f] += 1

print(fish_dict)

NUM_DAYS = 256
for x in range(NUM_DAYS):
  next_fish = dd(int)
  next_fish = {w-1:fish_dict[w] for w in range(1, 9)}
  if 0 not in next_fish:
    next_fish[0] = 0
  if 8 not in next_fish:
    next_fish[8] = 0
  next_fish[8] += fish_dict[0]
  next_fish[6] += fish_dict[0]
  print(next_fish, x)
  fish_dict = next_fish

print(sum(fish_dict.values()))