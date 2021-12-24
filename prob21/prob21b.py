from collections import defaultdict as dd
from pprint import pprint
from typing import Dict, Generator, List, Mapping, Optional, Tuple

from utils import stream_lines
from dirac import DiracState


 


file = 'prob21.in'
#file = 'scratch.txt'
lines = open(file).read().strip().split('\n')
p1,p2 = map(int, [x[-1] for x in lines])

initial_state = DiracState(p1,p2,(0,0))

#print(initial_state.handle_turn())


master_state = dict()
states: set[DiracState] = set()

master_state[initial_state] = 1
states.add(initial_state)


scores = [0,0]

while states:
  next_state = states.pop()
  if next_state.completed:
    winner = next_state.winner
    scores[winner] += master_state[next_state]
    master_state[next_state] = 0
    continue
  for state,times in next_state.handle_turn().items():
    if state not in master_state:
      master_state[state] = 0
    master_state[state] += times * master_state[next_state]
    states.add(state)
  master_state[next_state] = 0
  
print(scores, max(scores), sep='\n')

    
