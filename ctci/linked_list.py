class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

class LinkedList(object):
	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail
	
	def prepend(self, data):
		node = Node(data)
		node.next_node = self.head
		self.head = node
		print "prepend: " + str(self.head.data)


	def append(self, data):
		node = Node(data)
		current = self.head
		while current.next_node != None: # check to see if the next node is not none. if it is, then we are on the last node
			current = current.next_node
		current.next_node = node # add our node as the current node's next node
		self.tail = node
		print "append:" + str(self.tail.data)
	
	def delete(self, data):
		current = self.head
		if current.data == data:
			self.head = current.next_node
			current.next_node = None
			return

		current = self.head
		while current.next_node != None:
			if current.next_node.data == data:
				print "deleting: " + str(current.next_node.data)
				current.next_node = current.next_node.next_node
				return
			current = current.next_node
	def printValues(self):
		print "---"
		current = self.head
		while current != None:
			print current.data
			current = current.next_node
		print "---"
				

	
linked_list = LinkedList()

linked_list.prepend(1)

linked_list.append(2)

linked_list.append(3)

linked_list.prepend(0)

linked_list.printValues()
