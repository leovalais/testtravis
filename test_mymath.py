from mymath import *

def test_fact1():
    assert fact(0) == 1
def test_fact2():
    assert fact(1) == 1
def test_fact3():
    assert fact(2) == 2
def test_fact4():
    assert fact(10) == 3628800

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
