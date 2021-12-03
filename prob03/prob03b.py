from collections import defaultdict as dd
from typing import List

from utils import stream_lines


d = dd(lambda: dd(int))
allbins = []
for line in stream_lines('prob03.in'):
  allbins.append(line)
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

def run_filter(allbins, pred):
  bins = allbins
  idx = 0
  while len(bins) != 1:
    num_ones = sum([1 for x in bins if x[idx] == "1"])
    num_zeros = len(bins) - num_ones
    bins = filter(pred(num_ones, num_zeros, idx), bins)
    bins = list(bins)
    idx += 1
  return bins[0]

def oxygen_pred(ones, zeros, idx):
  if ones >= zeros:
    def pred(item):
      return item[idx] == "1"
    return pred
  else:
    def pred(item):
      return item[idx] == "0"
    return pred

def co2_pred(ones, zeros, idx):
  if ones < zeros:
    def pred(item):
      return item[idx] == "1"
    return pred
  else:
    def pred(item):
      return item[idx] == "0"
    return pred


#print(eps)
#print(allbins[0])
oxy = run_filter(allbins, oxygen_pred)
print(oxy)
co2 = run_filter(allbins, co2_pred)
print(co2)

oxy_num = binlist_to_int(oxy)
co2_num = binlist_to_int(co2)
print(oxy_num * co2_num)



