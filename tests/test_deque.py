import pytest
from Data.deque import Deque

def test_deque_append_pop_left_right():
    d = Deque()
    d.append_right(1)
    d.append_right(2)
    d.append_left(0)
    assert d.pop_left() == 0
    assert d.pop_right() == 2
    assert d.pop_left() == 1

def test_deque_is_empty():
    d = Deque()
    assert d.is_empty()
    d.append_left(42)
    assert not d.is_empty()
    d.pop_right()
    assert d.is_empty()

def test_deque_peek_left_right():
    d = Deque()
    d.append_right('a')
    d.append_left('b')
    assert d.peek_left() == 'b'
    assert d.peek_right() == 'a'

def test_deque_empty_exceptions():
    d = Deque()
    with pytest.raises(IndexError):
        d.pop_left()
    with pytest.raises(IndexError):
        d.pop_right()
    with pytest.raises(IndexError):
        d.peek_left()
    with pytest.raises(IndexError):
        d.peek_right()
