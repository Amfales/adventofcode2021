def windowed_box(grid: list[list[str]], fill_char:str):
  len1 = len(grid)
  len2 = len(grid[0])
  def lookup(a,b):
    if a < 0 or a >= len1:
      return fill_char
    if b < 0 or b >= len2:
      return fill_char
    return grid[a][b]
  
  for y in range(-2, len1):
    for x in range(-2, len2):
      l = []
      for w in range(3):
        l.append([])
        for z in range(3):
          l[-1].append(lookup(y+w, x+z))
      yield l
    
class Refiner():
  def __init__(self, algo_line: str):
    self.line = algo_line
    
  def _convert(self, subsection: list[list[str]]):
    assert len(subsection) == 3
    assert all([len(subsection[i]) == 3 for i in range(3)])
    s = 0
    for line in subsection:
      for item in line:
        s *= 2
        s += 1 if item == "#" else 0
    return s
  
  def get_pixel(self, subsection: list[list[str]]):
    spot = self._convert(subsection)
    return self.line[spot]


class Picture():
  def __init__(self, grid, refiner: Refiner, *, fill_char="."):
    self.grid = grid
    self.fill_char = fill_char
    self.ref = refiner
    
  def enhance(self) -> 'Picture':
    next_grid = []
    len1 = len(self.grid)
    len2 = len(self.grid[0])
    boxes = windowed_box(self.grid, self.fill_char)
    for y in range(len1+2):
      next_grid.append([])
      for x in range(len2+2):
        box = next(boxes)
        next_grid[-1].append(self.ref.get_pixel(box))
    
    outside = [[self.fill_char for x in range(3)] for y in range(3)]
    next_fill = self.ref.get_pixel(outside)
    return Picture(next_grid, self.ref, fill_char=next_fill)
  
  def print_grid(self):
    print("\n".join(["".join(line) for line in self.grid]))
    
    
    
