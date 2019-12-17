"""https://www.hackerrank.com/challenges/swap-nodes-algo/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=search

Complete the swapNodes function in the editor below. It should return a two-dimensional array where each element is an array of integers representing the node indices of an in-order traversal after a swap operation.

swapNodes has the following parameter(s):
- indexes: an array of integers representing index values of each , beginning with , the first element, as the root.
- queries: an array of integers, each representing a  value.
"""
from collections import deque

class Node():
    def __init__(self, index):
        self.index = index
        self.left = None
        self.right = None

def swap(root, t):
    """swap nodes at level t
    """
    def deep(current_node, level, t):
        if not current_node: return
        deep(current_node.left, level+1, t)
        deep(current_node.right, level+1, t)
        if (level+1)%t == 0:
            # post traversal... because if we make the swap and then recurse weird stuff happens
            # print(f'swaping at {current_node.index}, {current_node.left} <-> {current_node.right}')
            current_node.left, current_node.right = current_node.right, current_node.left
    return deep(root, level=0, t=t)

def build_tree(indexes):
    """build tree from an array of values
    """
    root = Node(1)
    queue = deque()
    queue.append(root)
    for i_l, i_r in indexes:
        node = queue.popleft()
        if i_l != -1:
            node.left = Node(i_l)
            queue.append(node.left)
        if i_r != -1:
            node.right = Node(i_r)
            queue.append(node.right)
    return root

def swapNodes(indexes, queries):
    # print(f'indexes: {indexes}')
    # with the complete binary tree representation we can do the operations...
    root = build_tree(indexes)
    # auxiliar method to traverse the tree
    res = []
    def traverse(root):
        """traverse the tree
        """
        def deep(current_node, level):
            if not current_node: return
            deep(current_node.left, level+1)
            # print('\t'*level, f'-->({current_node.index})')
            res.append(current_node.index)
            deep(current_node.right, level+1)
        return deep(root, level=0)
    # do the swaps
    output = []
    for q in queries:
        res = []
        # traverse(root)
        swap(root, q)
        traverse(root)
        output.append(res)
    return output

# test
indexes = [[2, 3],
        [-1, 4],
        [-1, 5],
        [-1, -1],
        [-1, -1]]

indexes = [[2, 3],
        [4, -1],
        [5, -1],
        [6, -1],
        [7, 8],
        [-1, 9],
        [-1, -1],
        [10, 11],
        [-1, -1],
        [-1, -1],
        [-1, -1]]

queries = [2]
print(f'testing with: {indexes}')
print(f'ans: {swapNodes(indexes, queries)}')
