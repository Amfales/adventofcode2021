import copy
import re
import string
from collections import defaultdict as dd
from pprint import pprint
from typing import Dict, Generator, List, Optional, Tuple

from snail import SnailExpression, parse_expression
from utils import stream_lines

file = 'prob18.in'
#file = 'scratch.txt'
line_gen = stream_lines(file)
exprs = [parse_expression(line) for line in line_gen]


big_mag = -1
for a in exprs:
  for b in exprs:
    temp_a, temp_b = copy.deepcopy(a), copy.deepcopy(b)
    c = temp_a + temp_b
    mag = c.get_magnitude()
    if mag > big_mag:
      #print(list(c), mag)
      big_mag = mag
      
print(big_mag)
