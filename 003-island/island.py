def random_walk(from, to):
  """
  This is a random walk along a single 'segment of a coastline' (defined by its start and end points.)
  Each endpoint is an x, y tuple on a cartesian plane. The random walk should never cross itself and
  never curve back towards its origin. Each step should be towards the end, even if only a little.
  """
  current_point = from
  all_points = [from]
  while current_point[0] != to[0] or current_point[1] != to[1]:
    pass
  
  return all_points

def main():
  descScr = "a script for generating islands with fractal coastlines"
  pass

if __name__ == '__main__':
    main()
   