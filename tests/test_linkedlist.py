import pytest
from Data.linkedlist import LinkedList

def test_insert_head():
    ll = LinkedList()
    ll.insert_head(1)
    ll.insert_head(2)
    assert ll.head and ll.head.value == 2
    assert ll.tail and ll.tail.value == 1
    assert len(ll) == 2

def test_insert_tail():
    ll = LinkedList()
    ll.insert_tail(1)
    ll.insert_tail(2)
    assert ll.head and ll.head.value == 1
    assert ll.tail and ll.tail.value == 2
    assert len(ll) == 2

def test_insert_mid():
    ll = LinkedList()
    ll.insert_tail(1)
    ll.insert_tail(3)
    ll.insert_mid(1, 2)
    assert ll.head and ll.head.value == 1
    assert ll.head and ll.head.next and ll.head.next.value == 2
    assert ll.tail and ll.tail.value == 3
    assert len(ll) == 3

def test_delete_head():
    ll = LinkedList()
    ll.insert_tail(1)
    ll.insert_tail(2)
    removed = ll.delete_head()
    assert removed == 1
    assert ll.head and ll.head.value == 2
    assert len(ll) == 1

def test_delete_tail():
    ll = LinkedList()
    ll.insert_tail(1)
    ll.insert_tail(2)
    removed = ll.delete_tail()
    assert removed == 2
    assert ll.tail and ll.tail.value == 1
    assert len(ll) == 1

def test_delete_head_empty():
    ll = LinkedList()
    with pytest.raises(IndexError):
        ll.delete_head()

def test_delete_tail_empty():
    ll = LinkedList()
    with pytest.raises(IndexError):
        ll.delete_tail()

def test_insert_mid_out_of_bounds():
    ll = LinkedList()
    with pytest.raises(IndexError):
        ll.insert_mid(1, 10)
    with pytest.raises(IndexError):
        ll.insert_mid(-1, 10)

def test_is_empty():
    ll = LinkedList()
    assert ll.is_empty()
    ll.insert_head(1)
    assert not ll.is_empty()
    ll.delete_head()
    assert ll.is_empty()
