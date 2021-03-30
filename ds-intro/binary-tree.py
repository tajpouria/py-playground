class Node:
	data = None
	left = None
	right = None

	def __init__(self, data):
		self.data = data

	def insert(self, node):
		if node.data <= self.data:
			if not self.left:
				self.left = node
				return
			
			self.left.insert(node)
			return

		if not self.right:
			self.right = node
			return 

		self.right.insert(node)


	def print_inorder(self):
		if self.left:
			self.left.print_inorder()	
		print(self.data)
		if self.right:
			self.right.print_inorder()
	

	def print_pretorder(self):
		print(self.data)
		if self.left:
			self.left.print_inorder()
		if self.right:
			self.right.print_postorder()


	def print_postorder(self):
		if self.left:
			self.left.print_inorder()
		if self.right:
			self.right.print_postorder()
		print(self.data)

	def contains(self, data):
		print(f"Checking {self.data}")
		if data == self.data:
			return True
		
		if data < self.data:
			if self.left:
				return self.left.contains(data)
		elif self.right:
			return self.right.contains(data)
		
		return False


n = Node(4)
n.insert(Node(3))
n.insert(Node(5))
n.insert(Node(5))
n.insert(Node(4))
n.insert(Node(6))
n.insert(Node(6))
n.insert(Node(7))

n.print_inorder()

print(n.contains(15))

n.print_postorder()
