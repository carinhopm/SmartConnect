import pytest
from random import randrange
import requests

from binarytree.insertion import runHttpServer, stopHttpServer, insert

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

def test_API():
    server = runHttpServer()
    sendPOST(None, 5)
    stopHttpServer(server)


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

def sendPOST(tree, value):
    body = {"value": value, "tree": tree }
    resp = requests.post('http://localhost:8080/insert', json=body)
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('POST /insert {}'.format(resp.status_code))
    for todo_item in resp.json():
        print("JSON Response: "+todo_item)
