def multiply(*args):
  ret = 1
  for a in args:
    ret *= a
  return ret

def return_if_jake(**kwargs):
  if not 'jake' in kwargs.keys():
   return False
  return kwargs['jake']

def call_with_42(func):
  return func(42)

def call_with_42_and_more(func, *args):
  return func(42, *args)

def get_water_function():
  def inner_func(seed):
    return 'water' + seed

  return inner_func

def run_transformations(op1, op2, *args):
  return [f(op1, op2) for f in args]
