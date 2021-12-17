from collections import defaultdict as dd
from typing import Generator, List, Dict, Tuple, Optional
from pprint import pprint
import string
import re

from utils import stream_lines

BitStream = Generator[str,None,None]

hex_lookup = {
  '0' : '0000',
  '1' : '0001',
  '2' : '0010',
  '3' : '0011',
  '4' : '0100',
  '5' : '0101',
  '6' : '0110',
  '7' : '0111',
  '8' : '1000',
  '9' : '1001',
  'A' : '1010',
  'B' : '1011',
  'C' : '1100',
  'D' : '1101',
  'E' : '1110',
  'F' : '1111',
}


def get_literal_value(bitstream: BitStream):
  real_bits = []
  while True:
    next_bits = get_bitpart(bitstream, 5)
    real_bits.append(next_bits[1:])
    if next_bits[0] == '0':
      break
  return ''.join(real_bits)

class Packet():
  subpackets: Optional[list['Packet']] = None
  version: str
  type_id: str
  lit_value: Optional[str] = None
  length_type: Optional[str] = None

  def __repr__(self):
    return str(self)

  def __str__(self):
    extra = ""
    if self.subpackets is not None:
      extra = f"subpackets -> Count({len(self.subpackets)})"
    else:
      extra = f"literal_value={self.lit_value}"
    return f"<Packet version={self.version} type_id={self.type_id} {extra}>"

  @classmethod
  def get_packet(cls, hexline: str) -> 'Packet':
    bitstream = hexstr_to_bitstream(hexline)
    p = Packet()
    p.version = get_bitpart(bitstream, 3)
    p.type_id = get_bitpart(bitstream, 3)
    p.parse_packet(bitstream)
    return p

  def parse_packet(self, bitstream: BitStream):
    if self.type_id == '100': # type_id 4 (Literal)
      self.lit_value = get_literal_value(bitstream)
    else:
      length_type = get_bitpart(bitstream, 1)
      self.length_type = length_type
      subpackets = []
      if length_type == '0':
        length_str = get_bitpart(bitstream, 15)
        length = int(length_str, 2)
        all_data = get_bitpart(bitstream, length)
        part_bitstream = bitstr_to_bitstream(all_data)
        running_length = 0
        while running_length < length:
          cur_packet = Packet()
          cur_packet.version = get_bitpart(part_bitstream, 3)
          cur_packet.type_id = get_bitpart(part_bitstream, 3)
          cur_packet.parse_packet(part_bitstream)
          running_length += cur_packet.get_rawsize()
          subpackets.append(cur_packet)
      elif length_type == '1':
        count_str = get_bitpart(bitstream, 11)
        count = int(count_str, 2)
        for x in range(count):
          cur_packet = Packet()
          cur_packet.version = get_bitpart(bitstream, 3)
          cur_packet.type_id = get_bitpart(bitstream, 3)
          cur_packet.parse_packet(bitstream)
          subpackets.append(cur_packet)
      self.subpackets = subpackets

  def get_rawsize(self):
    val = 0
    val += 6 # Version and TypeId
    if self.lit_value is not None:
      val += int(5/4 * len(self.lit_value))
    elif self.length_type is not None:
      val += 1 # Length id type
      if self.length_type == '0':
        val += 15 # Length value
      elif self.length_type == '1':
        val += 11
      for packet in self.subpackets:
        val += packet.get_rawsize()
    return val
        



def hexstr_to_bitstream(line: str):
  for char in line:
    for bit in hex_lookup[char]:
      yield bit

def bitstr_to_bitstream(line: str):
  for bit in line:
    yield bit

def get_bitpart(bitstream: BitStream, length: int):
  return ''.join([next(bitstream) for x in range(length)])




file = 'prob16.in'
#file = 'scratch.txt'
line = open(file).read().strip()
print(line[:10])

pack = Packet.get_packet(line)

def rec_add_versions(packet: Packet) -> int:
  s = 0
  s += int(packet.version, 2)
  if packet.subpackets is not None:
    for subpacket in packet.subpackets:
      s += rec_add_versions(subpacket)
  return s

print(rec_add_versions(pack))