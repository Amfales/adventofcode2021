from collections import defaultdict as dd
from typing import List

from utils import stream_lines

class BingoBoard():
  def __init__(self, nums: List[List[int]]):
    self.nums = nums
    self._lookupLoc = dict()
    self._numSet = set()
    self._numsAdded = set()
    self._board = dd(lambda: False)
    for x in range(5):
      for y in range(5):
        self._numSet.add(nums[x][y])
        self._lookupLoc[nums[x][y]] = (x,y)

  def addNum(self, num):
    if num not in self._numSet:
      return
    self._numsAdded.add(num)
    self._board[self._lookupLoc[num]] = True

  def hasWon(self):
    if len(self._numsAdded) < 5:
      return False
    for x in range(5):
      # Checking rows
      if all([self._board[(x,y)] for y in range(5)]):
        return True
    for y in range(5):
      # Checking cols
      if all([self._board[(x,y)] for x in range(5)]):
        return True
    
    # Check main diagonal
    if all([self._board[(x,x)] for x in range(5)]):
      return True
    
    # Check off diagonal
    if all([self._board[(x,5-x)] for x in range(5)]):
      return True

    return False

  def getScore(self, num):
    base = sum(self._numSet.difference(self._numsAdded))
    return base * num

  def __repr__(self):
    return str(self)

  def __str__(self):
    return f"<BingoBoard nums={str(self.nums)}>"


all_lines = list(stream_lines('prob04.in'))
num_order = list(map(int, all_lines[0].split(',')))

raw_bingos = []
for x in range(1, len(all_lines), 6):
  raw_bingo = []
  for row in all_lines[x+1:x+6]:
    raw_bingo.append([int(item) for item in row.split(' ') if item != ''])
  raw_bingos.append(raw_bingo)

all_bingos = [BingoBoard(x) for x in raw_bingos]

winning_board = None
idx = 0
cur_bingos = all_bingos[:]
while len(cur_bingos) != 1:
  curNum = num_order[idx]
  new_bingos = []
  for board in cur_bingos:
    board.addNum(curNum)
    if not board.hasWon():
      new_bingos.append(board)
  cur_bingos = new_bingos
  idx += 1

winning_board = cur_bingos[0]
while not winning_board.hasWon():
  curNum = num_order[idx]
  winning_board.addNum(curNum)
  idx += 1
  



print(winning_board)
print(idx)
print(num_order[:idx])
print(num_order[idx-1])
for x in range(5):
  for y in range(5):
    print(winning_board._board[(x,y)], end=' ')
  print()

print(winning_board.getScore(num_order[idx-1]))

