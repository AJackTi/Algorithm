class node:
	def __init__(self,data=None):
		self.data=data
		self.next=None

class linked_list:
	# self.head luu tat ca cac bien next cua node do
	# node head ban dau chi chua next: node 1->n, va data cua no = 0
	def __init__(self):
		self.head=node()

	# Adds new node containing 'data' to the end of the linked list.
	def append(self,data):
		new_node=node(data)
		cur=self.head
		while cur.next!=None:
			cur=cur.next
		cur.next=new_node

	# Returns the length (integer) of the linked list.
	def length(self):
		cur=self.head
		total=0
		while cur.next!=None:
			total+=1
			cur=cur.next
		return total 

	# Prints out the linked list in traditional Python list format. 
	def display(self):
		elems=[]
		cur_node=self.head
		while cur_node.next!=None:
			cur_node=cur_node.next
			elems.append(cur_node.data)
			
		print elems

	# Returns the value of the node at 'index'. 
	def get(self,index):
		if index>=self.length():
			print "ERROR: 'Get' Index out of range!"
			return None
		cur_idx=0
		cur_node=self.head
		while True:
			cur_node=cur_node.next
			if cur_idx==index: return cur_node.data
			cur_idx+=1

	# Deletes the node at index 'index'.
	def erase(self,index):
		if index>=self.length():
			print "[-] ERROR: 'Erase' Index out of range!"
			return 
		cur_idx=0
		cur_node=self.head
		while True:
			last_node=cur_node
			cur_node=cur_node.next
			if cur_idx==index:
				last_node.next=cur_node.next
				return
			cur_idx+=1

	# Allows for bracket operator syntax (i.e. a[0] to return first item).
	def __getitem__(self,index):
		return self.get(index)

	# Insert one element into linked list:
	def insert(self, index, data):
		new_node = node(data)
		cur = self.head
		if index > self.length():
			print "[-] ERROR: 'Erase' Index out of range!"
			return
		cur_index = 0
		while True:
			last_node = cur
			cur = cur.next
			if cur_index == index:
				last_node.next = new_node
				new_node.next = cur
				return
			cur_index += 1						
		

my_list = linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

print my_list.length()

my_list.display()

my_list.erase(2)

my_list.display()

my_list.insert(4, 10)

my_list.display()

print my_list.get(2)