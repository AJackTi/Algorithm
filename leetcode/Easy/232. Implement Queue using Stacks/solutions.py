# class Node:
#     def __init__(self, value) -> None:
#         self.value = value
#         self.next = None

# class MyQueue:
#     def __init__(self) -> None:
#         self.length = 0
        
#     def push(self, x: int) -> None:
#         if self.length == 0:
#             new_node = Node(x)
#             self.first = new_node
#             self.last = new_node
#             self.length = 1
#             return 
#         new_node = Node(x)
#         if self.first is None:
#             self.first = new_node
#             self.last = new_node
#         else:
#             self.last.next = new_node
#             self.last = new_node
#         self.length += 1
        
#     def pop(self) -> int:
#         if self.length == 0:
#             return -1
#         temp = self.first
#         if self.length == 1:
#             self.first = None
#             self.last = None
#         else:
#             self.first = self.first.next
#             temp.next = None
            
#         self.length -= 1
#         return temp.value

#     def peek(self) -> int:
#         if self.length == 0:
#             return -1
        
#         return self.first.value

#     def empty(self) -> bool:
#         return self.length == 0


class MyQueue:
    def __init__(self):
        self.queue = []
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        return self.queue.pop(0)
        

    def peek(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        return len(self.queue) == 0
        

# Your MyQueue object will be instantiated and called as such:
x = 1
obj = MyQueue()
obj.push(x)
obj.push(x)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()