infile = 'prob1.in'

text = None
with open(infile) as f:
  text = f.read()

lines = [x for x in text.split('\n') if x != '']
val = 0
for x in range(1, len(lines)):
  a,b = map(int, [lines[x-1], lines[x]])
  if b > a:
    val += 1

print(val)
