class Heap(object):

	HEAP_SIZE = 10

	def __init__(self):
		self.heap = [0]*Heap.HEAP_SIZE
		self.currentPosition = -1

	def insert(self, item):
		if self.isFull():
			print("Heap is full...")
			return

		self.currentPosition = self.currentPosition + 1
		self.heap[self.currentPosition] = item
		self.fixUp(self.currentPosition)
	
	def fixUp(self, index):
		parrentIndex = int((index-1)/2)
		while parrentIndex >= 0 and self.heap[parrentIndex] < self.heap[index]:
			temp = self.heap[index]
			self.heap[index] = self.heap[parrentIndex]
			self.heap[parrentIndex] = temp
			parrentIndex = int((index-1)/2)
	
	def heapsort(self):
		for i in range(0, self.currentPosition+1):
			temp = self.heap[0]
			print(str(temp))
			self.heap[0] = self.heap[self.currentPosition-i]
			self.heap[self.currentPosition-i]=temp
			self.fixDown(0, self.currentPosition-i-1)

	def fixDown(self, index, upto):
		while index <= upto:
			leftChild = 2*index+1
			rightChild = 2*index+2

			if leftChild < upto:
				childToSwap = None

				if rightChild > upto:
					childToSwap = leftChild
				else:
					if self.heap[leftChild] > self.heap[rightChild]:
						childToSwap = leftChild
					else:
						childToSwap = rightChild
				
				if self.heap[index] < self.heap[childToSwap]:
					temp = self.heap[index]
					self.heap[index] = self.heap[childToSwap]
					self.heap[childToSwap] = temp
				else:
					break

				index = childToSwap
			else:
				break

	def isFull(self):
		if self.currentPosition	== Heap.HEAP_SIZE:
			return True
		else:
			return False

if __name__ == "__main__":
	heap = Heap()
	heap.insert(10)
	heap.insert(-20)
	heap.insert(0)
	heap.insert(2)

	heap.heapsort()
	# print(heap.currentPosition)