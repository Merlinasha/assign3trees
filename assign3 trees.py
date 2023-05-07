#Implement Binary tree
class BinaryTree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if self.value:
            if data < self.value:
                if self.left is None:
                    self.left = BinaryTree(value)
                else:
                    self.left.insert(value)
            elif data > self.value:
                if self.right is None:
                    self.right = BinaryTree(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

root = BinaryTree(100)
root.insert(50)
root.insert(55)
root.insert(60)
root.insert(20)
root.insert(52)

root.PrintTree()

#Find height of a given tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
def height(root):
 
  
    if root is None:
        
        return 0 
    
    leftAns = height(root.left)
    rightAns = height(root.right)
 
    
    return max(leftAns, rightAns) + 1
 

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
 
print("Height of the binary tree is: " )

#Perform Pre-order, Post-order, In-order traversal
  #portorder
class node:
    def __init__(self,key) :
        self.right=None
        self.left=None
        self.key=key
def Postorder(root) :
    if root :
        Postorder(root.left) 
        Postorder(root.right)
        print(root.key,end=" ")                     
root=node(30)
root.left=node(20)
root.right=node(40)
root.left.left=node(15)
root.left.right=node(25)       
Postorder(root)
print()

        
  #pre order
class node:
    def __init__(self,key) :
        self.right=None
        self.left=None
        self.key=key
def Postorder(root) :
    if root :
        Postorder(root.left) 
        Postorder(root.right)
        print(root.key,end=" ")                     
root=node(30)
root.left=node(20)
root.right=node(40)
root.left.left=node(15)
root.left.right=node(25)       
Postorder(root)
print()
        
  #In order
class node:
    def __init__(self,key) :
        self.right=None
        self.left=None
        self.key=key
def Inorder(root): 
    if root: 
        Inorder(root.left) 
        print(root.key,end=" ")
        Inorder(root.right) 
root=node(30)
root.left=node(20)
root.right=node(40)
root.left.left=node(15)
root.left.right=node(25)       
Inorder(root)
print()


# Function to print all the leaves in a given binary tree
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def printLeafNodes(root: Node) -> None:

	if (not root):
		return

	if (not root.left and
		not root.right):
		print(root.data,
			end = " ")
		return

	if root.left:
		printLeafNodes(root.left)

	if root.right:
		printLeafNodes(root.right)

if __name__ == "__main__":

	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.right.left = Node(5)
	root.right.right = Node(8)
	root.right.left.left = Node(6)
	root.right.left.right = Node(7)
	root.right.right.left = Node(9)
	root.right.right.right = Node(10)

	printLeafNodes(root)

#Implement BFS (Breath First Search) and DFS (Depth First Search)
 # DFS (Depth First Search) 
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() 

def dfs(visited, graph, node):  
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Following is the Depth-First Search")
dfs(visited, graph, '5')
 
 #BFS (Breath First Search)
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() 

def dfs(visited, graph, node):  
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

#Find sum of all left leaves in a given Binary Tree

class Node:
	def __init__(self, k):
		self.data = k
		self.left = None
		self.right = None
		
def sumAllLeftLeaves(node, isleft):

	if node is None:
		return 0
		
	if node.left is None and node.right is None and isleft:
		return node.data

	
	return sumAllLeftLeaves(node.left, True) + sumAllLeftLeaves(node.right, False)


root = Node(20)
root.left = Node(9)
root.right = Node(49)
root.left.right = Node(12)
root.left.left = Node(5)
root.right.left = Node(23)
root.right.right = Node(52)
root.left.right.right = Node(12)
root.right.right.left = Node(50)

print("The sum of leaves is " + str(sumAllLeftLeaves(root, False)))

#Find sum of all nodes of the given perfect binary tree

import math
def sumNodes(l):
	
	leafNodeCount = math.pow(2, l - 1)
	sumLastLevel = 0
	sumLastLevel = ((leafNodeCount *(leafNodeCount + 1)) / 2)
	sum = sumLastLevel * l
	return int(sum)
l = 3
print (sumNodes(l))

#Count subtress that sum up to a given value x in a binary tree
class getNode:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

def countSubtreesWithSumX(root, count, x):
	if (not root):
		return 0
	ls = countSubtreesWithSumX(root.left,count, x)
	rs = countSubtreesWithSumX(root.right,count, x)
	Sum = ls + rs + root.data

	if (Sum == x):
		count[0] += 1
	return Sum

def countSubtreesWithSumXUtil(root, x):

	if (not root):
		return 0

	count = [0]
	ls = countSubtreesWithSumX(root.left,count, x)
	rs = countSubtreesWithSumX(root.right,count, x)

	if ((ls + rs + root.data) == x):
		count[0] += 1
	return count[0]

if __name__ == '__main__':

	root = getNode(5)
	root.left = getNode(-10)
	root.right = getNode(3)
	root.left.left = getNode(9)
	root.left.right = getNode(8)
	root.right.left = getNode(-4)
	root.right.right = getNode(7)
	x = 7
	print("Count =",
		countSubtreesWithSumXUtil(root, x))

#Find maximum level sum in Binary Tree
from collections import deque
class Node:
	def __init__(self, key):
		
		self.data = key
		self.left = None
		self.right = None

def maxLevelSum(root):
	if (root == None):
		return 0

	result = root.data
	q = deque()
	q.append(root)
	
	while (len(q) > 0):
		count = len(q)
		sum = 0
		while (count > 0):
			temp = q.popleft()
			sum = sum + temp.data
			if (temp.left != None):
				q.append(temp.left)
			if (temp.right != None):
				q.append(temp.right)
				
			count -= 1
		result = max(sum, result)
	return result

if __name__ == '__main__':
	
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.right = Node(8)
	root.right.right.left = Node(6)
	root.right.right.right = Node(7)

	print("Maximum level sum is", maxLevelSum(root))

#Print the nodes at odd levels of a tree
class newNode:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

def printOddNodes(root, isOdd = True):
	if (root == None):
		return
	if (isOdd):
		print(root.data, end = " ")
	printOddNodes(root.left, not isOdd)
	printOddNodes(root.right, not isOdd)

if __name__ == '__main__':
	root = newNode(1)
	root.left = newNode(2)
	root.right = newNode(3)
	root.left.left = newNode(4)
	root.left.right = newNode(5)
	printOddNodes(root)






	




