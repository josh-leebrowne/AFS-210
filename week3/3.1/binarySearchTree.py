from collections import deque 

def print_tree(root, data="data", left="left", right="right"):
    def display(root, data=data, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, data)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, data)
            u = len(s)
            first_line = (x + 1) * '\u2001' + (n - x - 1) * '_' + s
            second_line = x * '\u2001' + '/' + (n - x - 1 + u) * '\u2001'
            shifted_lines = [line + u * '\u2001' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, data)
            u = len(s)
            first_line = s + x * '_' + (n - x) * '\u2001'
            second_line = (u + x) * '\u2001' + '\\' + (n - x - 1) * '\u2001'
            shifted_lines = [u * '\u2001' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, data)
        u = len(s)
        first_line = (x + 1) * '\u2001' + (n - x - 1) * '_' + s + y * '_' + (m - y) * '\u2001'
        second_line = x * '\u2001' + '/' + (n - x - 1 + u + y) * '\u2001' + '\\' + (m - y - 1) * '\u2001'
        if p < q:
            left += [n * '\u2001'] * (q - p)
        elif q < p:
            right += [m * '\u2001'] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * '\u2001' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, data, left, right)
    for line in lines:
        print(line)
        
        
# Binary Tree
# – A tree where each node can have at most two children, often referred to as left and right child.
                
# Binary Search Tree
# - For a given node with a value, all the nodes in the left sub-tree are less than or equal 
# to the value of that node. While, all the nodes in the right sub-tree of this node are greater
# than that of the parent node.        

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left
                    if current is None:
                        parent.left = node
                        return
                else:
                    current = current.right
                    if current is None:
                        parent.right = node
                        return

    def search(self, data):
        current = self.root
        while True:
            if current is None:
                return False
            elif current.data is data:
                return True
            elif current.data > data:
                current = current.left
            else:
                current = current.right  

    def searchRec(self,current,data):
        if current is None:
            return False
        elif current.data is data:
            return True
        elif current.data > data:
            return self.searchRec(current.left,data)
        else:
            return self.searchRec(current.right,data)

# Depth-First Traverals
# 	- Follow a branch to its end, then climb upwards to continue the traversal
# 	- There are three forms of a depth-first traversal.
		

# PreOrder 
# 	- Visit root node first
# 	- Recursively do a preorder traversal of the left subtree
# 	- Recursively do a preorder traversal of the right subtree
#
#	- Results = 5 3 1 4 6 8 7 9
	
# InOrder
# 	- Recursively do a inorder traversal of the left subtree
# 	- Visit root node first
# 	- Recursively do a inorder traversal of the right subtree
#
#	- Results = 1 3 4 5 6 7 8 9

# PostOrder
# 	- Recursively do a postorder traversal of the left subtree
# 	- Recursively do a postorder traversal of the right subtree
# 	- Visit root node first	
#	
#	- Results = 1 4 3 7 9 8 6 5

# Breadth-First Traversal
# 	- Start at the root of a tree and visit every node from one level of the tree to the next.
# 	- So instead of going up and down the tree, we visit every node on a level before 
#		going down to the next level.


    def breadth_first_traversal(self):
        list_of_nodes = []
        traversal_queue = deque([self.root])
        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()
            list_of_nodes.append(node.data)
            if node.left:
                traversal_queue.append(node.left)
            if node.right:
                traversal_queue.append(node.right)
        return list_of_nodes


bsTree = BinaryTree()
bsTree.insert(5)
bsTree.insert(3)
bsTree.insert(6)
bsTree.insert(1)
bsTree.insert(4)
bsTree.insert(8)
bsTree.insert(7)
bsTree.insert(9)

print_tree(bsTree.getRoot())

print("Value is stored on the tree? "+str(bsTree.search(8))) #(On)

print(bsTree.searchRec(bsTree.getRoot(),4)) #(On)

print(bsTree.breadth_first_traversal())