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



a = exprs[0]
for b in exprs[1:]:
  a = a + b
      
print(a.get_magnitude())
