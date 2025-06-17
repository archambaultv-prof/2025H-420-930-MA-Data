import pytest
from Data.lifo import LIFO

def test_lifo_push_pop():
    s = LIFO()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1

def test_lifo_is_empty():
    s = LIFO()
    assert s.is_empty()
    s.push(42)
    assert not s.is_empty()
    s.pop()
    assert s.is_empty()

def test_lifo_peek():
    s = LIFO()
    s.push('a')
    assert s.peek() == 'a'
    s.push('b')
    assert s.peek() == 'b'
    s.pop()
    assert s.peek() == 'a'

def test_lifo_empty_exceptions():
    s = LIFO()
    with pytest.raises(IndexError):
        s.pop()
    with pytest.raises(IndexError):
        s.peek()
