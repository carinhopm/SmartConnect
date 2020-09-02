# SmartConnect Student Challenge
This repo contains the solution for the parts 1 & 2 of the SmartConnect Student Challenge, 
consisting on the implementation of the operation _insert_ for a Binary Search Tree (BST).

## Technnical details
The challenge has been implemented using Python 3.7 as programming language. 
This implementation can be found in the file _src/binarytree/insertion.py_.

Within the folder _tests_ it can be found the file _test_insertion.py_ containing two tests:

- Test A: which basically builds a simple BST with low values 
and check the correct position of the nodes just after the additions.
- Test B: that builds a BST with 50 nodes with random keys for its nodes 
and checks that every node has a left child with a lower key and 
a right child with a higher key (in case it has children).

These tests are being runned by Travis-CI everytime a new commit is pushed. The Travis-CI configuration can be found in the file _.travis.yml_, 
which prepares the environment and runs the Python file _setup.py_ 
containing the information to run the tests.
