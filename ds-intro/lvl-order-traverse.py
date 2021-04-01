from collections import deque

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


def lvl_order_insert(root, vals):
	q = deque([root])	

	for lv, rv in vals:
		n = q.popleft()
		if lv is not None:
			n.left = Node(lv)
			q.append(n.left)
		if rv is not None:
			n.right = Node(rv)
			q.append(n.right)
	
	return root


def lvl_order_print(root):
	q = deque([root])	

	while len(q) > 0:
		n = q.popleft()
		print(n.val)
		if n.left is not None:
			q.append(n.left)
		if n.right is not None:
			q.append(n.right)


r = Node(1)
r = lvl_order_insert(r, [[2,3], [4,5], [6,7], [8,None], [None,None], [10, 11]])
lvl_order_print(r)

