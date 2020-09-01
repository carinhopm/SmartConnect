import pytest
from random import randrange

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

def test_B():
    keys = list()
    root = None
    while len(keys)<50:
        num = randrange(100)
        if num not in keys:
            keys.append(num)
            root = insert(root, num, None)
    for key in keys:
        assert(checkNode(root, key) == True)


def checkNode(root, key):
    if root.key == key:
        if root.left is not None and root.left.key >= key:
            return False
        if root.right is not None and root.right.key <= key:
            return False
        return True
    elif root.key > key:
        return checkNode(root.left, key)
    else:
        return checkNode(root.right, key)
