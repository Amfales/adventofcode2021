from collections import defaultdict as dd
from typing import Generator, List, Dict, Tuple, Optional
from pprint import pprint
import string
import re

from utils import stream_lines

file = 'prob17.in'
#file = 'scratch.txt'
line = open(file).read().strip()
parts = line.strip('target area: ').split(', ')
x_bounds,y_bounds = [[int(part) for part in piece.split('=')[1].split('..')] for piece in parts]

def xseries(x_vel: int):
  x = 0
  cur_vel = x_vel
  while True:
    yield x
    x += cur_vel
    if cur_vel != 0:
      cur_vel = (cur_vel - 1) if cur_vel >= 0 else (cur_vel + 1)

def yseries(y_vel: int):
  y = 0
  cur_vel = y_vel
  while True:
    yield y
    y += cur_vel
    cur_vel -= 1

def get_trajectory(x_vel: int, y_vel: int):
  x_gen = xseries(x_vel)
  y_gen = yseries(y_vel)
  while True:
    yield (next(x_gen), next(y_gen))


def filter_box(x_bounds: Tuple[int,int], y_bounds: Tuple[int,int]):
  def inner_func(x_vel:int, y_vel: int):
    trajectory = get_trajectory(x_vel, y_vel)
    prev_x = None
    prev_y = None
    y_going_down = False
    while True:
      next_x,next_y = next(trajectory)
      if prev_x is not None and next_x == prev_x:
        if not (x_bounds[0] <= next_x <= x_bounds[1]):
          return False
        if next_y < y_bounds[0] and y_going_down:
          return False
        
      if x_bounds[0] <= next_x <= x_bounds[1]:
        if y_bounds[0] <= next_y <= y_bounds[1]:
          return True

      if prev_y is not None and prev_y > next_y:
        y_going_down = True
      prev_x,prev_y = next_x,next_y
    return False
  return inner_func

def triangle_nums():
  s = 1
  diff = 1
  while True:
    yield s
    s += diff
    diff += 1
    
box = filter_box(x_bounds, y_bounds)
s = set()
for x_vel in range(250):
  for y_vel in range(-1000,1500):
    if box(x_vel,y_vel):
      s.add((x_vel, y_vel))
    print(x_vel,y_vel)

print(len(s))