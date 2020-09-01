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
        insert(root.left, key, value)
    else:
        insert(root.right, key, value)
    return root