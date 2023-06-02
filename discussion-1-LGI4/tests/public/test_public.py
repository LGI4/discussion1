from hof import *

def test_is_present():
  a = []
  b = ["w","x","y","z"]
  c = [14,20,42,1,81]

  assert [] == is_present(a,123), "is_present 1"
  assert [0,0,1,0] == is_present(b,"y"), "is_present 2"
  assert [0,0,1,0,0] == is_present(c,42), "is_present 3"

def test_count_occ():
  a = [1,2,1,1,1,1]
  b = [False,True,True,True]
  c = []

  assert 5 == count_occ(a,1),"count_occ 1"
  assert 3 == count_occ(b,True), "count_occ 2"
  assert 0 == count_occ(c,"a"), "count_occ 3"

def test_uniq():
  a = [1,7,7,1,5,2,7,7]
  b = [True,False,False,True,False,False,False]
  c = []

  assert sorted([1,2,5,7]) == sorted(uniq(a)), "uniq 1"
  assert sorted([False,True]) == sorted(uniq(b)), "uniq 2"
  assert [] == uniq(c), "uniq 3"

def test_find_max():
  a = [[1,2,3,4,5] for i in range(5)]
  assert 5 == find_max(a), "find_max 1"

  a[2][2] = 10
  assert 10 == find_max(a), "find_max 2"

def test_count_ones():
  a = [[1,1,1,1,1] for i in range(3)]
  b = [[1,1,1,1,1] if i%2==0 else [0,0,0,0,0] for i in range(10)]
  
  assert 15 == count_ones(a), "count_ones 1"
  assert 25 == count_ones(b), "count_ones 2"

def test_addgen():
  f1 = addgenerator(5)
  f2 =  addgenerator(10)

  assert 8 == f1(3), "addgen 1"
  assert 23 == f1(3) + f2(5), "addgen 1"

def test_apply_to_self():

  assert 12 == apply_to_self()(3,lambda a: 3**2),"appy to self 1"

def test_ap():
  a = [1,2,3]
  fs = [lambda a: a + 1, lambda b: b-1]

  assert [2,3,4,0,1,2] == ap(fs,a)

def test_map2():
  m = [[1,2,3],[4,5,6],[7,8,9]]
  f = lambda x: x * 2
  assert [[2,4,6],[8,10,12],[14,16,18]] == map2(m,f), "map2 1"

  m2 = [[1,0,1],[1,0,1]]
  assert [[True,False,True],[True,False,True]] == map2(m2,lambda x: True if x == 1 else 0), "map2 2"
