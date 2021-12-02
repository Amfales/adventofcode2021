from utils import stream_lines

class Submarine():
  def __init__(self):
    self.forward = 0
    self.depth = 0
    self.aim = 0


sub = Submarine()
for line in stream_lines('prob02.in'):
  parts = line.split(' ')
  match parts:
    case ['forward', distance]:
      val = int(distance)
      sub.forward += val
      sub.depth += val * sub.aim
    case ['up', distance]:
      val = int(distance)
      sub.aim -= val
    case ['down', distance]:
      val = int(distance)
      sub.aim += val

print(sub.forward, sub.depth)
print(sub.forward * sub.depth)

