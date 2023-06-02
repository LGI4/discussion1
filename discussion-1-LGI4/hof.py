from functools import reduce
def is_present(lst,x):
  return list(map(lambda a: 1 if a == x else 0, lst));

def count_occ(lst,target):
  return reduce(lambda a,h: a + 1 if h == target else a, lst,0);

def uniq(lst):
  return reduce(lambda a,h: a+[h] if count_occ(a,h) == 0 else a,lst,[])

def find_max(matrix):
  return reduce(lambda a,b: reduce(lambda c,d: max(c,d),b,a),matrix,0) # b is list from outer reduce

def count_ones(matrix):
  return reduce(lambda a,b: reduce(lambda c,d: c + 1 if d == 1 else c,b,a),matrix,0)

def addgenerator(x):
  return lambda a: a + x

def apply_to_self():
  return lambda a,b: a + b(a)

def ap(fns,args):
  return reduce(lambda acc, fn: acc + list(map(fn, args)), fns, [])

def map2(matrix,f):
  return [list(map(f, h)) for h in matrix]
