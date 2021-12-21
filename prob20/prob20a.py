import copy
from functools import lru_cache
import re
import string
from collections import defaultdict as dd
from pprint import pprint
from typing import Dict, Generator, List, Mapping, Optional, Tuple
import statistics

from utils import stream_lines
from picture import Refiner, Picture






file = 'prob20.in'
#file = 'scratch.txt'
algo, img = open(file).read().strip().split('\n\n')
grid = img.split('\n')

print(grid)

r = Refiner(algo)
pic = Picture(grid, r)

s = 0
for line in two_refine.grid:
  for item in line:
    if item == "#":
      s += 1
      
print(s)
