from collections import defaultdict as dd

from utils import stream_lines

def is_lowpoint(lines, pt):
  len1, len2 = len(lines), len(lines[0])
  x,y = pt
  non_diag_diffs = [(0,1), (0,-1), (-1,0), (1,0)]
  non_diag_pts = [(x+a[0],y+a[1]) for a in non_diag_diffs]
  #diffs = [(x+a,y+b) for a in (-1,0,1) for b in (-1,0,1) if not (a == 0 and b==0)]
  for point in non_diag_pts:
    if point[0] < 0 or point[0] >= len1:
      continue
    if point[1] < 0 or point[1] >= len2:
      continue
    
    if lines[point[0]][point[1]] <= lines[x][y]:
      return False
  
  return True

def floodfill(lines, low_pt):
  len1, len2 = len(lines), len(lines[0])
  
  pts = [low_pt]

  non_diag_diffs = [(0,1), (0,-1), (-1,0), (1,0)]

  seen = set()
  num_pts = 0
  while pts:
    cur_pt = pts.pop()
    for pt in [(cur_pt[0]+a[0], cur_pt[1]+a[1]) for a in non_diag_diffs]:
      if pt[0] < 0 or pt[0] >= len1:
        continue
      if pt[1] < 0 or pt[1] >= len2:
        continue
      if pt not in seen:
        seen.add(pt)
        if lines[pt[0]][pt[1]] != 9:
          pts.append(pt)
          num_pts += 1
  
  return num_pts


file = 'prob09.in'
lines = [[int(x) for x in line] for line in stream_lines(file)]
len1, len2 = len(lines), len(lines[0])
print(len1,len2)
m = [[False for y in range(len2)] for x in range(len1)]
low_pts = []
for x in range(len1):
  for y in range(len2):
    if is_lowpoint(lines, (x,y)):
      low_pts.append((x,y))

d: dict[tuple[int,int], int] = dict()
for pt in low_pts:
  d[pt] = floodfill(lines, pt)


bigs = list(sorted([item for item in d.values()]))
last_three = bigs[-3:]
val = 1
for item in last_three:
  print(item)
  val *= item
print(val)