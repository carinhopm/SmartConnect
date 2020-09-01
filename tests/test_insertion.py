import pytest

from binarytree.insertion import insert

def test_A():
    root = insert(None,10,None)
    assert(root.key == 10)
    root = insert(root,15,None)
    assert(root.right.key == 15)
    root = insert(root,5,None)
    assert(root.left.key == 5)
    root = insert(root,12,None)
    assert(root.right.left.key == 12)
    root = insert(root,8,None)
    assert(root.left.right.key == 8)
    root = insert(root,17,None)
    assert(root.right.right.key == 17)
    root = insert(root,11,None)
    assert(root.right.left.left.key == 11)

'''def test_B():
	assert(insert(None,15,None).key == 10)

def test_C():
	assert(insert(None,15,None).key == 10)'''