import pytest
from Data.fifo import FIFO

def test_fifo_enqueue_dequeue():
    f = FIFO()
    f.enqueue(1)
    f.enqueue(2)
    f.enqueue(3)
    assert f.dequeue() == 1
    assert f.dequeue() == 2
    assert f.dequeue() == 3

def test_fifo_is_empty():
    f = FIFO()
    assert f.is_empty()
    f.enqueue(42)
    assert not f.is_empty()
    f.dequeue()
    assert f.is_empty()

def test_fifo_peek():
    f = FIFO()
    f.enqueue('a')
    assert f.peek() == 'a'
    f.enqueue('b')
    assert f.peek() == 'a'
    f.dequeue()
    assert f.peek() == 'b'

def test_fifo_empty_exceptions():
    f = FIFO()
    with pytest.raises(IndexError):
        f.dequeue()
    with pytest.raises(IndexError):
        f.peek()
