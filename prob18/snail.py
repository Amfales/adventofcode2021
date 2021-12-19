from typing import Iterable, Optional,Any, Literal
from ast import literal_eval

class SnailExpression():
  should_autobalance: bool = True
  
  
  parent: Optional['SnailExpression'] = None
  left: Optional['SnailExpression'] | int = None
  right: Optional['SnailExpression'] | int = None

  def __init__(self,
               parent: Optional['SnailExpression'] = None,
               left_val: Optional['SnailExpression'] | int = None,
               right_val: Optional['SnailExpression'] | int = None):
    self.parent = parent
    self.left = left_val
    self.right = right_val
    
  def is_leftchild(self):
    if self.parent is None:
      return None
    return self.parent.left is self
  
  def is_rightchild(self):
    if self.parent is None:
      return None
    return self.parent.right is self
    
  @property
  def depth(self) -> int:
    if self.parent is None:
      return 0
    return self.parent.depth + 1
  
  @property
  def height(self) -> int:
    if isinstance(self.left, self.__class__):
      if isinstance(self.right, self.__class__):
        return max(self.left.height, self.right.height) + 1
      return self.left.height + 1
    elif isinstance(self.right, type(self)):
      return self.right.height + 1
    return 0
  
  @property
  def root(self) -> 'SnailExpression':
    cur = self
    while cur.parent is not None:
      cur = cur.parent
    return cur
  
  
  def inorder_neighbors(self, center: 'SnailExpression') -> tuple['SnailExpression','SnailExpression','SnailExpression']:
    nodes = [item for item in self._inorder()]
    if center is nodes[0]:
      return (None, center, nodes[1])
    elif center is nodes[-1]:
      return (nodes[-2], center, None)
    else:
      for n1,n2,n3 in zip(nodes,nodes[1:],nodes[2:]):
        if center is n2:
          return (n1,n2,n3)
    return (None,None,None)
  
  def _inorder(self) -> Iterable['SnailExpression']:
    def helper(expr: SnailExpression):
      l,r = isinstance(expr.left, SnailExpression),isinstance(expr.right, SnailExpression)
      if l:
        yield from helper(expr.left)
        if r:
          yield from helper(expr.right)
        else:
          yield expr
      else:
        yield expr
        if r:
          yield from helper(expr.right)
    yield from helper(self.root)
    
  
  def should_explode(self) -> bool:
    """Should be called on the root node"""
    return self.height >= 4
  
  def get_exploder(self) -> 'SnailExpression':
    for item in self._inorder():
      if item.depth >= 4:
        l,r = isinstance(item.left,int),isinstance(item.right, int)
        if l and r:
          return item
    return None
  
  def _handle_exploder(self):
    exploder = self.get_exploder()
    a,_,c = self.inorder_neighbors(exploder)
    if a is not None:
      if isinstance(a.right, int):
        a.right += exploder.left
      elif isinstance(a.left, int):
        a.left += exploder.left
    if c is not None:
      if isinstance(c.left, int):
        if isinstance(exploder.right, exploder.__class__):
          print(list(exploder))
        c.left += exploder.right
      elif isinstance(c.right, int):
        c.right += exploder.right
        
    if exploder.is_leftchild():
      exploder.parent.left = 0
      del exploder
    elif exploder.is_rightchild():
      exploder.parent.right = 0
      del exploder
      
  
  def should_split(self) -> bool:
    """Should be called on the root node"""
    for item in self._inorder():
      if isinstance(item.left, int):
        if item.left >= 10:
          return True
      if isinstance(item.right, int):
        if item.right >= 10:
          return True
    return False
  
  def get_splitter(self) -> tuple['SnailExpression', bool]:
    assert self.should_split()
    for item in self._inorder():
      if isinstance(item.left, int):
        if item.left >= 10:
          return item, True
      if isinstance(item.right, int):
        if item.right >= 10:
          return item, False
    assert False
    
  def _handle_splitter(self):
    splitter, on_left = self.get_splitter()
    if on_left:
      l = splitter.left // 2
      r = splitter.left - l
      splitter.left = SnailExpression(splitter, l, r)
    else:
      l = splitter.right // 2
      r = splitter.right - l
      splitter.right = SnailExpression(splitter, l, r)
    
    
  def balance(self, *, debug_print=False):
    if debug_print:
      print(list(self.root), self.root, sep='\n')
    while True:
      while self.should_explode():
        self._handle_exploder()
        if debug_print:
          print("e", list(self.root), self.root)
      if self.should_split():
        self._handle_splitter()
        if debug_print:
          print("s", list(self.root))
        
      if not self.should_explode() and not self.should_split():
        break
      
    if debug_print:
      print(list(self.root))
      
      
  def get_magnitude(self) -> int:
    """Only call this on root"""
    def helper(expr: SnailExpression) -> int:
      l,r = isinstance(expr.left, int), isinstance(expr.right, int)
      s = 0
      s += 3 * (expr.left if l else helper(expr.left))
      s += 2 * (expr.right if r else helper(expr.right))
      return s
    
    return helper(self.root)
    
    
    
  def __repr__(self):
    return str(self)
  
  def __str__(self):
    return f"<SnailExpression height={self.height} depth={self.depth} left={self.left} right={self.right}>"

  def __add__(self, other):
    val = SnailExpression(None, self, other)
    self.parent = val
    other.parent = val
    if self.should_autobalance:
      val.balance()
    return val
  
  def __iter__(self):
    l = list(self.left) if isinstance(self.left, type(self)) else self.left
    r = list(self.right) if isinstance(self.right, type(self)) else self.right
    yield l
    yield r
      
    
  
    

    
def to_snail_expression(data: tuple[Any|int,Any|int], parent: Optional[SnailExpression] = None) -> SnailExpression:
  assert len(data) == 2
  match data:
    case (int() as x, int() as y):
      return SnailExpression(parent, x, y)
    case (int() as x, y):
      p = SnailExpression(parent, x, None)
      right = to_snail_expression(y, p)
      p.right = right
      return p
    case (x, int() as y):
      p = SnailExpression(parent, None, y)
      left = to_snail_expression(x, p)
      p.left = left
      return p
    case (x,y):
      p = SnailExpression(parent)
      left = to_snail_expression(x, p)
      p.left = left
      right = to_snail_expression(y, p)
      p.right = right
      return p
      
    
def parse_expression(line: str) -> SnailExpression:
  data = literal_eval(line)
  return to_snail_expression(data)