class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

	def add_next(self, next):
		self.next = next

	def add_as_next(self, prev):
		prev.next = self

	def get_next(self):
		return self.next

	def __str__(self):
		n = self
		p = str()
		while n:
			p += str(n.value) + "->"
			n = n.next
		return p
	def reverse(self, sofar=None):
		#print(sofar)
		if not self:
			return sofar
		todo = self.next
		self.next = sofar
		sofar = self
		if todo:
			x = todo.reverse(sofar)
		else:
			x = sofar
		return x

if __name__ == "__main__":
	head = None
	for index in range(1,100):
		n = Node(index)
		n.add_next(head)
		head = n
	print(head)
	x = head.reverse(None)
	print(x)
