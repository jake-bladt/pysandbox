def factorial(n):
  r = 1
  for x in range(1, n):
    r *= (x + 1)

  return r
