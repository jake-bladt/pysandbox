from collections import defaultdict

def get_next_sequence():
  i = 1
  yield i
  i += 1

def get_constant():
  return 42

sequences = defaultdict(get_constant)

print(sequences['this'])
print(sequences['that'])
