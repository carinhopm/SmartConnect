#!/usr/bin/python

"""
Insertion function
"""
def insert(root, key, value):
    if root==None:
        root = Node(key, value)
    elif key==root.key:
        root.value = value
    elif key<root.key:
        root.left = insert(root.left, key, value)
    else:
        root.right = insert(root.right, key, value)
    return root

"""
Node object
"""
class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.element = value
        self.left = None
        self.right = None
