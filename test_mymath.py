from mymath import *

def test_fact1():
    assert fact(0) == 1
def test_fact2():
    assert fact(1) == 1
def test_fact3():
    assert fact(2) == 2
def test_fact4():
    assert fact(10) == 3628800
def test_fact5():
    assert fact(-12) == -1

def test_inc1():
    assert inc(0) == 1
def test_inc2():
    assert inc(1) == 2
def test_inc3():
    assert inc(1) == 2
def test_inc4():
    assert inc(10) == 11
def test_inc5():
    assert inc(-15) == -14
def test_inc6():
    assert inc(-15, 15) == 0
def test_inc7():
    assert inc(15, -15) == 0

from random import randint
MAXINT = 2 ** 31
COUNT = 100

def test_negabs1():
    assert negabs(15) == -15
def test_negabs2():
    assert negabs(-15) == -15
def test_negabs3():
    assert negabs(1) == -1
def test_negabs4():
    assert negabs(0) == 0
def test_negabs5():
    assert negabs(-0) == 0
def test_negabs6():
    assert negabs(-0) == negabs(0)
def test_negabs_idem():
    for _ in range(COUNT):
        x = randint(-MAXINT, MAXINT)
        assert negabs(negabs(x)) == negabs(x)
def test_negabs_randneg():
    for _ in range(COUNT):
        x = randint(0, MAXINT)
        assert negabs(x) == -x
def test_negabs_randpos():
    for _ in range(COUNT):
        x = randint(-MAXINT, 0)
        assert negabs(x) == x
