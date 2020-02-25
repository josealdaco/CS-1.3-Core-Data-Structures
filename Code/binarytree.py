#!python
from collections import deque


class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # TODO: Check if both left child and right child have no value
        if self.right is None and self.left is None:
            return True
        return False

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # TODO: Check if either left child or right child has a value
        if self.right is not None or self.left is not None:
            return True
        return False

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""
        # TODO: Check if left child has a value and if so calculate its height
        # TODO: Check if right child has a value and if so calculate its height
        # Return one more than the greater of the left height and right height
        left_height = 0
        right_height = 0
        node = self
        node_List = []
        while True:
            if node.left is not None and node.right is not None:
                node_List.append((node, "right"))
            if node.left is not None:
                if node.right is None:
                    left_height += 1
                    node = node.left
                else:
                    left_height += 1
                    node = node.left
            if node.right is not None:
                if node.left is None:
                    right_height += 1
                    node = node.right
                else:
                    right_height += 1
                    node = node.right
            if node.right is None and node.left is None:
                if len(node_List) == 0:
                    """ Only break if there is no more top nodes to redirect"""
                    print("left", left_height, "right", right_height)
                    if left_height >= right_height:
                        return left_height
                    else:
                        return right_height
                else:
                    """ Give the node of the first tuple of nodes"""
                    if node_List[0][1] == "right":
                        node = node_List[0][0].right
                    node_List.pop()


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""
        # TODO: Check if root node has a value and if so calculate its height
        return self.root.height()

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)

        # Return True if a node as found, or False
        if node is not None:
            return True
        return False

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # TODO: Return the node's data if found, or None
        if node is not None:
            return node
        return None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Handle the case where the tree is empty
        if self.is_empty():
            # TODO: Create a new root node
            self.root = BinaryTreeNode(item)
            # TODO: Increase the tree size
            self.size += 1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_iterative(item)#, self.root)
        if parent.is_branch():
            if parent.left is not None:
                parent.right = BinaryTreeNode(item)
            else:
                parent.left = BinaryTreeNode(item)
        if parent.is_leaf():
            if item > parent.data:
                parent.right = BinaryTreeNode(item)
            else:
                parent.left = BinaryTreeNode(item)

        self.size += 1
        return

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Start with the root node
        node = self._find_parent_node_iterative(item)
        if node is None:
            return None
        if node.data == item:
            return node.data
        if node.left is not None and node.left.data == item:
            return node.left.data
        elif node.right is not None:
            return node.right.data
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        node = self._find_parent_node_recursive(item, node)
        if node is None:
            return None
        if node.data == item:
            return node.data
        if node.left is not None:
            return self._find_node_recursive(item, node.left)
        else:
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = node
        if self.is_empty() is True or self.root is None:
            return parent
        while node is not None:
            parent_Full = True
            if node.data == item:
                return parent
            if node.left is None and node.right is not None or node.right is None and node.left is not None:
                parent_Full = False
            if node.is_leaf() is True or parent_Full is False:
                """  If there are no branches or only has a single branch"""
                return parent
            if item < node.data:
                """ Parent will be left node"""
                parent = node.left
                node = node.left
            else:
                parent = node.right
                node = node.right

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        # # Check if starting node exists
        if node is None:
            return None
        # # TODO: Check if the given item matches the node's data
        if node.data == item and parent is None:
            return node
        elif node.data == item and parent is not None:
            return parent
        # TODO: Check if the given item is less than the node's data
        elif item < node.data:
            parent = node.left
            # TODO: Recursively descend to the node's left child, if it exists
            return self._find_parent_node_recursive(item, node.left, parent)
        # TODO: Check if the given item is greater than the node's data
        elif item > node.data:
            parent = node.right
            # TODO: Recursively descend to the node's right child, if it exists
            return self._find_parent_node_recursive(item, node.right, parent)

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # TODO: Use helper methods and break this algorithm down into 3 cases
        # based on how many children the node containing the given item has and
        # implement new helper methods for subtasks of the more complex cases

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        if node is not None:
            # TODO: Traverse left subtree, if it exists
            self._traverse_in_order_recursive(node.left, visit)
            # TODO: Visit this node's data with given function
            visit(node.data)
            # TODO: Traverse right subtree, if it exists
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse in-order without using recursion (stretch challenge)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Visit this node's data with given function
        if node is not None:
            visit(node.data)
        # TODO: Traverse left subtree, if it exists
            self._traverse_pre_order_recursive(node.left, visit)
        # TODO: Traverse right subtree, if it exists
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        if node is not None:
            # TODO: Traverse left subtree, if it exists
            self._traverse_post_order_recursive(node.left, visit)
            # TODO: Traverse right subtree, if it exists
            self._traverse_post_order_recursive(node.right, visit)
            # TODO: Visit this node's data with given function
            visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Create queue to store nodes not yet traversed in level-order
        queue = deque()
        # TODO: Enqueue given starting node
        queue.append(start_node)
        # TODO: Loop until queue is empty
        while len(queue) > 0:
            # TODO: Dequeue node at front of queue
            node = queue.popleft()
            # TODO: Visit this node's data with given function
            visit(node.data)
            # TODO: Enqueue this node's left child, if it exists
            if node.left is not None:
                queue.append(node.left)
            # TODO: Enqueue this node's right child, if it exists
            if node.right is not None:
                queue.append(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
