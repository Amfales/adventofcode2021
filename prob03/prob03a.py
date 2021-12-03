from collections import defaultdict as dd
from typing import List

from utils import stream_lines


d = dd(lambda: dd(int))
for line in stream_lines('prob03.in'):
  for i,bit in enumerate(line):
    d[i][bit] += 1

eps,gamma = [],[]
for i in range(len(d)):
  if d[i]["1"] > d[i]["0"]:
    eps.append("1")
    gamma.append("0")
  else:
    eps.append("0")
    gamma.append("1")

print(eps, gamma)

def binlist_to_int(binlist: List[str]):
  val = 0
  for x in binlist:
    val *= 2
    val += int(x)
  return val

beps = binlist_to_int(eps)
bgamma = binlist_to_int(gamma)
print(beps, bgamma, beps*bgamma)