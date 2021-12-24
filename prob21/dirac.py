class DiracState:
  p1_pos: int
  p2_pos: int
  scores: tuple[int,int]
  is_p1_turn: bool
  
  def __init__(self, p1_pos, p2_pos, scores, is_p1_turn=True):
    self.p1_pos = p1_pos
    self.p2_pos = p2_pos
    self.scores = scores
    self.is_p1_turn = is_p1_turn
    
    
  @property
  def completed(self):
    return any([score >= 21 for score in self.scores])
  
  @property
  def winner(self):
    if self.completed:
      if self.scores[0] >= 21:
        return 0
      else:
        return 1
    
  def handle_turn(self) -> dict['DiracState', int]:
    d = dict()
    for a in range(1,4):
      for b in range(1,4):
        for c in range(1,4):
          s = self.move(a+b+c)
          if s not in d:
            d[s] = 0
          d[s] += 1
    assert sum(d.values()) == 27
    return d
  
  def move(self, dist: int) -> 'DiracState':
    base = self.p1_pos if self.is_p1_turn else self.p2_pos
    spot = base + dist
    while spot > 10:
      spot -= 10
    s1,s2 = self.scores
    next_scores = (s1+spot, s2) if self.is_p1_turn else (s1, s2+spot)
    next_p1 = spot if self.is_p1_turn else self.p1_pos
    next_p2 = self.p2_pos if self.is_p1_turn else spot
    return DiracState(next_p1, next_p2, next_scores, not self.is_p1_turn)
  
  def __hash__(self):
    return hash((self.p1_pos, self.p2_pos, self.scores, self.is_p1_turn))
  
  def __eq__(self, other: 'DiracState'):
    return ((self.p1_pos, self.p2_pos, self.scores, self.is_p1_turn) ==
            (other.p1_pos, other.p2_pos, other.scores, other.is_p1_turn))
    
    
  def __repr__(self):
    return str(self)
  
  def __str__(self):
    return f"<DiracState p1_pos={self.p1_pos} p2_pos={self.p2_pos} scores={self.scores} p1_turn={self.is_p1_turn}>"
  