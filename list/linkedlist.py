#### Using Python 2 to run ####
class Node(object):

	def __init__(self, data):
		self.data = data
		self.nextNode = None

class LinkedList(object):

	def __init__(self):
		self.head = None
		self.size = 0

	def insertStart(self, data):

		self.size = self.size + 1
		newNode = Node(data)

		if not self.head:
			self.head = newNode

		else:
			newNode.nextNode = self.head
			self.head = newNode

	def remove(self, data):
		# Check head of linked list None or Not
		if self.head is None:
			return

		self.size = self.size - 1

		currentNode = self.head
		previousNode = None

		while currentNode.data != data:
			previousNode = currentNode
			currentNode = currentNode.nextNode

		if previousNode is None:
			self.head = currentNode.nextNode
		else:
			previousNode.nextNode = currentNode.nextNode


	def length(self):
		return self.size

	def size2(self):

		actualNode = self.head
		size = 0

		while actualNode is not None:
			size += 1
			actualNode = actualNode.nextNode

		return size

	def insertEnd(self, data):

		self.size = self.size + 1
		newNode = Node(data)
		actualNode = self.head

		while actualNode.nextNode is not None:
			actualNode = actualNode.nextNode

		actualNode.nextNode = newNode

	def traverseList(self):

		actualNode = self.head

		while actualNode is not None:
			print "%d" %actualNode.data
			actualNode = actualNode.nextNode

print "Init LinkedList"
linkedlist = LinkedList()

# insert item into linkedlist
linkedlist.insertStart(12)
linkedlist.insertStart(122)
linkedlist.insertStart(3)
linkedlist.insertEnd(31)

print "Print Item:"
# print item if linkedlist
linkedlist.traverseList()
print "Length Of LinkedList Before Remove"
# print size of linkedlist
print linkedlist.length()

# Remove item in linked list
linkedlist.remove(31)
linkedlist.remove(12)
linkedlist.remove(122)
linkedlist.remove(3)

print "Length Of LinkedList After Remove"
print linkedlist.length()