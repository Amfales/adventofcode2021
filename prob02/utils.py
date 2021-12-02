def stream_lines(filename: str):
  with open(filename) as f:
    for line in f.readlines():
      if line != "":
        yield line