import heapq

"""Chapter 4: Trees and Graphs"""

class Node:

    """Tree Initializations"""
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()
        
    """Traversals"""
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def preorder(self, root, res):
        if not root:
            return
        res.append(root.data)
        self.preorder(root.left, res)
        self.preorder(root.right, res)

    """Height""" 
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            lDepth = self.maxDepth(root.left)
            rDepth = self.maxDepth(root.right)
            return 1 + max(lDepth, rDepth) 

    """4.2 Minimal Tree"""
    def minimalTree(self, list, start, end):
        if end <= start:
            return None
        mid = (end + start) // 2
        r = Node(list[mid])
        r.left = self.minimalTree(list, start, mid - 1)
        r.right = self.minimalTree(list, mid + 1, end)
        return r
    
    """4.3 List of Depths"""
    def listofdepths(self, root):
        queue = []
        queue.append(root)
        tree = [[root.data]]

        while queue:
            level = len(queue)
            nodes = []
            for i in range(level):
                curr = queue.pop(0)
                print(curr.data)
                if curr.left:
                    queue.append(curr.left)
                    nodes.append(curr.left.data)
                if curr.right:
                    queue.append(curr.right)
                    nodes.append(curr.right.data)
            tree.append(nodes)
        
        print(tree[:len(tree)-1])

    """4.4 Check Balanced"""
    def checkbalanced(self, root):
        if not root:
            return True
        leftH = self.maxDepth(root.left)
        rightH = self.maxDepth(root.right)
        if abs(leftH - rightH) > 1:
            return False
        return self.checkbalanced(root.left) and self.checkbalanced(root.right)

    """4.5 Validate BST"""        
    def validateBST(self, root):
        if not root:
            return True
        if root.left:
            if root.left.data > root.data:
                return False
        if root.right:
            if root.right.data < root.data:
                return False
        return self.validateBST(root.left) and self.validateBST(root.right)
        
    """4.8 First Common Ancestor"""
    def shortestpath(self, root):
        # if on same side, go down
        # if on opposite sides, must be at most common parent 



"""Heap"""
myHeap = []
heapq.heappush(myHeap, 4)
heapq.heappush(myHeap, 6)
heapq.heappush(myHeap, 2)
heapq.heappush(myHeap, 10)
heapq.heappush(myHeap, 3)
print(myHeap)
minimum = heapq.heappop(myHeap)
print(minimum)
list = [4, 3, 2, 4, 1, 3, 2]
heapq.heapify(list)
minimum2 = heapq.heappop(list)
print(minimum2)
print('\n')

print('depth: ')
root = Node(10)
root.insert(1)
root.insert(11)
d = root.maxDepth(root)
print(d)
print('\n')

print('4.2 minimal tree: ')
minList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = Node(0)
r = r.minimalTree(minList, 0, len(minList))
r.PrintTree()
d = r.maxDepth(r)
print('depth: ', d)
print('\n')

print('4.3 list of depth: ')
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.PrintTree()
print('\n')
root.listofdepths(root)
print('\n')

print('4.4 check balanced:')
root = Node(1)
root.right = Node(2)
root.left = Node(3)
root.right.right = Node(4)
res = root.checkbalanced(root)
print(res)
print('\n')

print('4.5 validate BST:')
root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.right.right = Node(4)
root.right.left = Node(3)
res = root.validateBST(root)
print(res)
print('\n')

print('4.8 First Common Ancestor:')
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.PrintTree()
print('\n')
root.shortestpath(root)
print('\n')