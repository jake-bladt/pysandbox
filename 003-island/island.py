import random

def random_walk(from, to, min_steps = 10, max_steps = 20, smoothing = 0.5):
  """
  This is a random walk along a single 'segment of a coastline' (defined by its start and end points.)
  Each endpoint is an x, y tuple on a cartesian plane. The random walk should never cross itself and
  never curve back towards its origin. Each step should be towards the end, even if only a little.
  """
  
  min_delta = (float(from[0]) / max_steps, float(from[1]) / max_steps)
  max_delta = (float(from[0]) / min_steps, float(from[1]) / min_steps)

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
   