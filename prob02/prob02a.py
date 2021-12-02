from utils import stream_lines

class Submarine():
  def __init__(self):
    self.forward = 0
    self.depth = 0


sub = Submarine()
for line in stream_lines('prob02.in'):
  parts = line.split(' ')
  match parts:
    case ['forward', distance]:
      sub.forward += int(distance)
    case ['up', distance]:
      sub.depth -= int(distance)
    case ['down', distance]:
      sub.depth += int(distance)

print(sub.forward, sub.depth)
print(sub.forward * sub.depth)

