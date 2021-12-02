from typing import Any, List


infile = 'prob1.in'

text = None
with open(infile) as f:
  text = f.read()

lines = [x for x in text.split('\n') if x != '']

def gen_in_parts(num_parts: int, l: List[Any]):
  for x in range(len(l) - num_parts + 1):
    yield l[x:x+num_parts]

parts_gen = gen_in_parts(3, lines)

a,b = next(parts_gen, None),next(parts_gen, None)
val = 0
while b != None:
  if sum(map(int, b)) > sum(map(int, a)):
    val += 1
  a,b = b, next(parts_gen, None)

print(val)




