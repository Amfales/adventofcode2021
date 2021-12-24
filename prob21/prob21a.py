from collections import defaultdict as dd
from pprint import pprint
from typing import Dict, Generator, List, Mapping, Optional, Tuple

from utils import stream_lines

class PracticeDie():
  cur_roll: int = 1
  times_rolled: int = 0
  
  def __next__(self):
    val = self.cur_roll
    self.cur_roll += 1
    if self.cur_roll > 100:
      self.cur_roll -= 100
      
    self.times_rolled += 1
    return val
    


def handle_turn(die, spot):
  amt = next(die) + next(die) + next(die)
  diff = amt % 10
  next_spot = spot + diff
  while next_spot > 10:
    next_spot -= 10
  return next_spot


file = 'prob21.in'
#file = 'scratch.txt'
lines = open(file).read().strip().split('\n')
p1,p2 = map(int, [x[-1] for x in lines])

pract_die = PracticeDie()

points = {
  1: 0,
  2: 0
}

while True:
  p1 = handle_turn(pract_die, p1)
  points[1] += p1
  if points[1] >= 1000:
    print(points[2] * pract_die.times_rolled)
    break
  
  p2 = handle_turn(pract_die, p2)
  points[2] += p2
  if points[2] >= 1000:
    print(points[1] * pract_die.times_rolled)
    break






