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

def get_multipliers(first = 1, last = 10, step = 1):
  coeff = first
  while coeff <= last:
    def multiplier(op):
      lc = int(coeff)
      return lc * op

    yield multiplier
    coeff += step

def traced_call(func):
  def new_func(*args):
    return {
      "name": func.__name__,
      "args": args,
      "result": func(*args)
    }

  return new_func

@traced_call
def traced_add(*args):
  return sum(args)
